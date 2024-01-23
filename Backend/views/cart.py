from flask import Blueprint, render_template, redirect, url_for, session, flash
from flask_login import current_user
from datetime import datetime, timedelta
from backend.views.models import Product, Inventory
from network.DBSTUFF import connection_string
import pyodbc

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

# Create a function to get a database connection
def get_db():
    return pyodbc.connect(connection_string)

@cart_bp.route('/add/<int:product_id>/<int:quantity>')
def add_to_cart(product_id, quantity):
    # Initialize the cart in the session if not exists
    session.setdefault('cart', {})

    # Check if cart cleanup is needed
    cleanup_cart()

    # Retrieve the product from the database
    with get_db() as connection:
        cursor = connection.cursor()

        # Fetch product details
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        product_row = cursor.fetchone()

        # Fetch inventory details
        cursor.execute("SELECT Inv FROM Inventory WHERE Prod_ID = ?", (product_id,))
        inventory_row = cursor.fetchone()

    if product_row and inventory_row:
        product = Product(*product_row)
        stock = inventory_row[0]

        # Check if there is enough stock
        if stock >= quantity:
            # Check if the product is already in the cart
            if product_id not in session['cart']:
                session['cart'][product_id] = {'name': product.Name, 'price': product.Price, 'quantity': 0, 'timestamp': datetime.utcnow()}

            # Update the quantity and timestamp
            session['cart'][product_id]['quantity'] += quantity
            session['cart'][product_id]['timestamp'] = datetime.utcnow()

            # Decrease the stock in the inventory
            new_stock = stock - quantity

            # Ensure atomic update of stock
            try:
                cursor.execute("UPDATE Inventory SET Inv = ? WHERE Prod_ID = ? AND Inv = ?", (new_stock, product_id, stock))
                connection.commit()
                flash(f"{quantity} {product.Name} added to the cart.", 'success')
            except pyodbc.IntegrityError:
                flash("Concurrency issue: Please try again.", 'danger')
        else:
            flash(f"Not enough stock for {product.Name}. Available stock: {stock}", 'danger')
    else:
        flash("Product not found or inventory information not available.", 'danger')

    return redirect(url_for('cart.view_cart'))


def cleanup_cart():
    # Cleanup cart by removing items that have been in the cart for more than 5 minutes
    current_time = datetime.utcnow()
    cart = session.get('cart', {})

    for product_id, item in list(cart.items()):
        timestamp = item.get('timestamp')

        if timestamp and (current_time - timestamp) > timedelta(minutes=5):
            # Return items to inventory
            quantity = item['quantity']
            with get_db() as connection:
                cursor = connection.cursor()

                # Fetch current stock
                cursor.execute("SELECT Inv FROM Inventory WHERE Prod_ID = ?", (product_id,))
                inventory_row = cursor.fetchone()

                if inventory_row:
                    current_stock = inventory_row[0]

                    # Update inventory
                    new_stock = current_stock + quantity
                    cursor.execute("UPDATE Inventory SET Inv = ? WHERE Prod_ID = ?", (new_stock, product_id))
                    connection.commit()

                    # Remove item from the cart
                    del cart[product_id]

                    flash(f"{quantity} {item['name']} returned to inventory due to inactivity.", 'warning')

    # Update the session cart
    session['cart'] = cart

@cart_bp.route('/view')
def view_cart():
    # Retrieve the cart from the session
    cart = session.get('cart', {})

    # Fetch product details for items in the cart
    products = []
    total_price = 0

    for product_id, item in cart.items():
        # Fetch product details
        with get_db() as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
            product_row = cursor.fetchone()

        if product_row:
            product = Product(*product_row)
            price = int(product.Price)

            products.append({
                'id': product.ID,
                'name': product.Name,
                'quantity': item['quantity'],
                'price': price,
                'subtotal': item['quantity'] * price
            })

            total_price += item['quantity'] * price
        else:
            flash(f"Product not found with ID: {product_id}", 'danger')

    return render_template('cart/view_cart.html', products=products, total_price=total_price)
