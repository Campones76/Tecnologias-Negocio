# your_app/routes.py
import os
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user
from backend.views.models import Category, Inventory, Product
from network.DBSTUFF import connection_string
import pyodbc


# Create a function to get a database connection
def get_db():
    return pyodbc.connect(connection_string)


products_bp = Blueprint('products', __name__, url_prefix='/products')


@products_bp.route('/computers')
def list_computers():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?",
            (1,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/computers.html', products=products)


@products_bp.route('/computers/<int:product_id>')
def view_computer(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            # Check if the product is in the current user's favorites
            cursor.execute("SELECT 1 FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?",
                           (current_user.id, product_id))
            is_favorite = cursor.fetchone() is not None
            return render_template('products/customer_view_product.html', product=product, is_favorite=is_favorite)
        return "Product not found", 404


@products_bp.route('/keyboards')
def list_keyboard():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?",
            (2,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/keyboards.html', products=products)


@products_bp.route('/keyboards/<int:product_id>')
def view_keyboard(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            # Check if the product is in the current user's favorites
            cursor.execute("SELECT 1 FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?",
                           (current_user.id, product_id))
            is_favorite = cursor.fetchone() is not None
            return render_template('products/customer_view_product.html', product=product, is_favorite=is_favorite)
        return "Product not found", 404


@products_bp.route('/mouse')
def list_mouse():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?",
            (3,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/mouses.html', products=products)


@products_bp.route('/mouse/<int:product_id>')
def view_mouse(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            # Check if the product is in the current user's favorites
            cursor.execute("SELECT 1 FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?",
                           (current_user.id, product_id))
            is_favorite = cursor.fetchone() is not None
            return render_template('products/customer_view_product.html', product=product, is_favorite=is_favorite)
        return "Product not found", 404


@products_bp.route('/display')
def list_display():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?",
            (4,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/displays.html', products=products)


@products_bp.route('/display/<int:product_id>')
def view_display(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            # Check if the product is in the current user's favorites
            cursor.execute("SELECT 1 FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?",
                           (current_user.id, product_id))
            is_favorite = cursor.fetchone() is not None
            return render_template('products/customer_view_product.html', product=product, is_favorite=is_favorite)
        return "Product not found", 404


@products_bp.route('/')
def list_products():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product")
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/list_products.html', products=products)


@products_bp.route('/Admin/<int:product_id>')
def admin_view_product(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/view_product.html', product=product)
        return "Product not found", 404


@products_bp.route('/<int:product_id>')
def view_product(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            # Check if the product is in the current user's favorites
            cursor.execute("SELECT 1 FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?",
                           (current_user.id, product_id))
            is_favorite = cursor.fetchone() is not None
            return render_template('products/customer_view_product.html', product=product, is_favorite=is_favorite)
        return "Product not found", 404


@products_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')

    with get_db() as connection:
        cursor = connection.cursor()

        # Fetch all categories from the 'Categories' table
        cursor.execute("SELECT ID, Name FROM Categories")
        categories = [Category(*row) for row in cursor.fetchall()]

    if request.method == 'POST':
        with get_db() as connection:
            cursor = connection.cursor()

            # Retrieve form data
            name = request.form['name']
            price = float(request.form['price'])
            category_id = int(request.form['category'])
            desc = request.form['desc']
            brand = request.form['brand']
            model = request.form['model']
            colour = request.form['colour']
            details = request.form['details']
            inventory_quantity = int(request.form['quantity'])

            # Save uploaded image
            image = request.files['image']
            image_file_name = f"{name}_image.jpg"
            image_path = os.path.join("frontend/static/images", image_file_name)
            image.save(image_path)

            # Insert the product into the 'Product' table
            cursor.execute("""
                INSERT INTO Product (Name, Price, CatID, Image, Description, Brand, Model, Colour, Details) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (name, price, category_id, image_file_name, desc, brand, model, colour, details))
            connection.commit()

            # Retrieve the ID of the newly inserted product
            cursor.execute("SELECT @@IDENTITY AS 'Identity';")
            product_id = cursor.fetchone()[0]

            if product_id:
                # Insert an entry into the 'Inventory' table with the specified quantity
                cursor.execute("""
                    INSERT INTO Inventory (Prod_ID, Inv) 
                    VALUES (?, ?)""",
                               (product_id, inventory_quantity))
                connection.commit()

        return redirect(url_for('products.list_products'))

    return render_template('products/add_product.html', categories=categories)


@products_bp.route('/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')

    with get_db() as connection:
        cursor = connection.cursor()

        # Fetch the product details for the specified product_id
        cursor.execute(
            "SELECT ID, Name, Price, CatID, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?",
            (product_id,))
        row = cursor.fetchone()
        if not row:
            return "Product not found", 404
        product = Product(*row)

        # Fetch inventory for the product
        cursor.execute("SELECT Inv FROM Inventory WHERE Prod_ID = ?", (product_id,))
        inventory_row = cursor.fetchone()
        inventory_count = inventory_row[0] if inventory_row else 0

        # Fetch all categories from the 'categories' table
        cursor.execute("SELECT ID, Name FROM Categories")
        categories = [Category(*row) for row in cursor.fetchall()]

        if request.method == 'POST':
            # Retrieve form data
            name = request.form.get('name')
            price = request.form.get('price', type=float)
            category_id = request.form.get('category', type=int)
            desc = request.form.get('desc')
            brand = request.form.get('brand')
            model = request.form.get('model')
            colour = request.form.get('colour')
            details = request.form.get('details')
            delete_product = request.form.get('delete_product')
            new_inventory_count = request.form.get('quantity', type=int)

            # Handle product deletion
            if delete_product:
                # First delete the inventory entry for the product
                cursor.execute("DELETE FROM Inventory WHERE Prod_ID = ?", (product_id,))
                connection.commit()

                # Delete the entry from the 'Favorites' table
                cursor.execute("DELETE FROM dbo.Favorites WHERE Prod_ID = ?", (product_id,))
                connection.commit()

                # Then delete the product itself
                cursor.execute("DELETE FROM Product WHERE ID = ?", (product_id,))
                connection.commit()

                return redirect(url_for('products.list_products'))

            # Handle image upload and other field updates
            update_fields = []
            update_values = []

            # Add fields to update list if they have changed
            if name and name != product.Name:
                update_fields.append("Name = ?")
                update_values.append(name)
            if price is not None and price != product.Price:
                update_fields.append("Price = ?")
                update_values.append(price)
            if category_id is not None and category_id != product.CatID:
                update_fields.append("CatID = ?")
                update_values.append(category_id)
            if desc and desc != product.Description:
                update_fields.append("Description = ?")
                update_values.append(desc)
            if brand and brand != product.Brand:
                update_fields.append("Brand = ?")
                update_values.append(brand)
            if model and model != product.Model:
                update_fields.append("Model = ?")
                update_values.append(model)
            if colour and colour != product.Colour:
                update_fields.append("Colour = ?")
                update_values.append(colour)
            if details and details != product.Details:
                update_fields.append("Details = ?")
                update_values.append(details)

            # Check if a new image file is provided
            if 'image' in request.files and request.files['image']:
                image = request.files['image']
                image_path = f"{product_id}_image.jpg"
                image.save(image_path)
                update_fields.append("Image = ?")
                update_values.append(image_path)

            # Perform update if there are fields to update
            if update_fields:
                update_statement = "UPDATE Product SET " + ", ".join(update_fields) + " WHERE ID = ?"
                update_values.append(product_id)
                cursor.execute(update_statement, update_values)
                connection.commit()

            # Update inventory if it has changed
            if new_inventory_count is not None and new_inventory_count != inventory_count:
                cursor.execute("UPDATE Inventory SET Inv = ? WHERE Prod_ID = ?", (new_inventory_count, product_id))
                connection.commit()

            return redirect(url_for('products.view_product', product_id=product_id))

    return render_template('products/edit_product.html', product=product, categories=categories,
                           inventory_count=inventory_count)
