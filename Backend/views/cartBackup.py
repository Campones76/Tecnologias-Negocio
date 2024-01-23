from decimal import Decimal
import random
import time
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


def generate_unique_cart_id():
    # Assuming current_user.id is the user's ID
    user_id = current_user.id if current_user.is_authenticated else 0  # Use 0 for guest (guest can't buy this is really just a last measure)

    # Using a combination of user_id, timestamp, and a random number for uniqueness
    timestamp = int(time.time())
    random_number = random.randint(1, 1000)

    unique_id = int(f"{user_id}{timestamp}{random_number}")

    return unique_id

def get_user_address(user_id):
    query = "SELECT Address FROM [User] WHERE ID = ?"
    
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result:
            return result[0]  # Assuming the address is in the first column of the result
        else:
            return None  # Return None if the user is not found or has no address

@cart_bp.route('/add/<int:product_id>/<int:quantity>')
def add_to_cart(product_id, quantity):
    # Initialize the cart in the session if it doesn't exist
    session.setdefault('cart', {})

    # Check if cart cleanup is needed
    cleanup_cart()

    # Retrieve the product from the DB
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


@cart_bp.route('/purchase', methods=['POST'])
def purchase_items():
    if not current_user.is_authenticated:
        flash("Please login to complete the purchase.", "danger")
        return redirect(url_for('signin_bp.login'))

    cart = session.get('cart', {})
    if not cart:
        flash("Your cart is empty.", "danger")
        return redirect(url_for('cart.view_cart'))

    try:
        with get_db() as connection:
            cursor = connection.cursor()

            # Generate a unique Cart_ID
            cart_id = generate_unique_cart_id()

            # Insert data into Purchases table and collect inserted IDs
            purchase_ids = []
            for product_id, item in cart.items():
                cursor.execute(
                    "INSERT INTO Purchases (User_ID, Prod_ID, Cart_ID, Total) VALUES (?, ?, ?, ?)", 
                    (current_user.id, product_id, cart_id, item['quantity'] * Decimal(item['price']))
                )
                purchase_ids.append(cursor.execute("SELECT @@IDENTITY").fetchval())

            # Fetch user's current address
            user_address = get_user_address(current_user.id)

            # Insert data into Purchase_History table
            for purchase_id in purchase_ids:
                cursor.execute(
                    "INSERT INTO Purchase_History (User_ID, Purchase_ID, Review_ID, Order_Status, User_Address) VALUES (?, ?, NULL, 1, ?)", 
                    (current_user.id, purchase_id, user_address)
                )

            connection.commit()

            # Clear the cart
            session['cart'] = {}

            flash("Purchase completed successfully.", "success")
            return redirect(url_for('cart.view_cart'))

    except Exception as e:
        flash(str(e), "danger")
        return redirect(url_for('cart.view_cart'))