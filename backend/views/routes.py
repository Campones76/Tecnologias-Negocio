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
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?", (1,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/computers.html', products=products)

@products_bp.route('/computers/<int:product_id>')
def view_computer(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/view_product.html', product=product)
        return "Product not found", 404

@products_bp.route('/keyboards')
def list_keyboard():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?", (2,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/keyboards.html', products=products)

@products_bp.route('/keyboards/<int:product_id>')
def view_keyboard(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/view_product.html', product=product)
        return "Product not found", 404

@products_bp.route('/mouse')
def list_mouse():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?", (3,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/mouses.html', products=products)

@products_bp.route('/mouse/<int:product_id>')
def view_mouse(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/view_product.html', product=product)
        return "Product not found", 404

@products_bp.route('/display')
def list_display():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE CatID = ?", (4,))
        products = [Product(*row) for row in cursor.fetchall()]

    return render_template('products/displays.html', products=products)

@products_bp.route('/display/<int:product_id>')
def view_display(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/view_product.html', product=product)
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
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
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
        cursor.execute("SELECT ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            product = Product(*row)
            return render_template('products/customer_view_product.html', product=product)
        return "Product not found", 404

@products_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()

        # Fetch all categories from the 'categories' table
        cursor.execute("SELECT ID, Name FROM Categories")
        categories = [Category(*row) for row in cursor.fetchall()]
        
        # Fetch all categories from the 'categories' table
        cursor.execute("SELECT ID, Prod_ID, Inv FROM Inventory")
        inventory = [Inventory(*row) for row in cursor.fetchall()]

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
            inventory = int(request.form['quantity'])

            # Save uploaded image
            image = request.files['image']
            image.save(f"frontend/static/images/{name}_image.jpg")  # Adjust the path as needed

            # Insert the product into the 'products' table
            cursor.execute("INSERT INTO Product (Name, Price, CatID, Image, Description, Brand, Model, Colour, Details) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (name, price, category_id, f"{name}_image.jpg", desc, brand, model, colour, details))
            connection.commit()
            
            # Retrieve the ID of the newly inserted product
            cursor.execute("SELECT SCOPE_IDENTITY()")
            product_id = cursor.fetchone()[0]
            # Insert an entry into the 'Inventory' table with the specified quantity
            # Insert or update the quantity in the 'Inventory' table
            cursor.execute("MERGE INTO Inventory AS target "
                           "USING (VALUES (?, ?)) AS source (Prod_ID, Inv) "
                           "ON target.Prod_ID = source.Prod_ID "
                           "WHEN MATCHED THEN "
                           "UPDATE SET target.Inv = source.Inv "
                           "WHEN NOT MATCHED THEN "
                           "INSERT (Prod_ID, Inv) VALUES (source.Prod_ID, source.Inv);",
                           (product_id, inventory))
            connection.commit()

            return redirect(url_for('products.list_products'))

    return render_template('products/add_product.html', categories=categories)

# @products_bp.route('/<int:product_id>/edit', methods=['GET', 'POST'])
# def edit_product(product_id):
#     with get_db() as connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT ID, Name, CatID, Price, Image FROM Product WHERE ID = ?", (product_id,))
#         row = cursor.fetchone()
#         if not row:
#             return "Product not found", 404

#         product = Product(*row)

#         if request.method == 'POST':
#             cursor.execute("UPDATE Product SET Name = ?, Price = ? WHERE ID = ?",
#                            (request.form['name'], float(request.form['price']), product.ID))
#             connection.commit()
#             return redirect(url_for('products.view_product', product_id=product.ID))
@products_bp.route('/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    with get_db() as connection:
        cursor = connection.cursor()

        # Fetch the product details for the specified product_id
        cursor.execute("SELECT ID, Name, Price, CatID, Image, Description, Brand, Model, Colour, Details FROM Product WHERE ID = ?", (product_id,))
        row = cursor.fetchone()
        if not row:
            return "Product not found", 404

        product = Product(*row)

        # Fetch all categories from the 'categories' and 'Inventory' table
        cursor.execute("SELECT ID, Name FROM Categories")
        categories = [Category(*row) for row in cursor.fetchall()]
        
        cursor.execute("SELECT ID, Prod_ID, Inv FROM Inventory")
        inventory = [Inventory(*row) for row in cursor.fetchall()]

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
            delete_product = request.form.get('delete_product')
            inventory = int(request.form['quantity'])

            if delete_product:
                # Delete the product and its image from the file system
                cursor.execute("DELETE FROM Product WHERE ID = ?", (product.ID,))
                connection.commit()

                # Delete the image file
                image_path = f"{name}_image.jpg"  # Adjust the path as needed
                if os.path.exists(image_path):
                    os.remove(image_path)

                return redirect(url_for('products.list_products'))
            # Check if a new image file is provided
            if 'image' in request.files:
                # Save uploaded image
                image = request.files['image']
                image_path = f"{name}_image.jpg"  # Adjust the path as needed
                image.save(image_path)

                # Update the 'Image' column in the 'Product' table
                cursor.execute("UPDATE Product SET Name = ?, Price = ?, CatID = ?, Image = ?, Description = ?, Brand = ?, Model = ?, Colour = ?, Details = ? WHERE ID = ?",
                               (name, price, category_id, image_path, desc, brand, model, colour, details, product.ID))
            else:
                # Update other product details without changing the image
                cursor.execute("UPDATE Product SET Name = ?, Price = ?, CatID = ?, Description = ?, Brand = ?, Model = ?, Colour = ?, Details = ? WHERE ID = ?",
                               (name, price, category_id, desc, brand, model, colour, details, product.ID))
            
            connection.commit()
            # Update the quantity in the 'Inventory' table
            #cursor.execute("UPDATE Inventory SET Inv = ? WHERE Prod_ID = ?", (quantity, product.ID))
                        # Insert or update the quantity in the 'Inventory' table
            # Insert or update the quantity in the 'Inventory' table
            cursor.execute("MERGE INTO Inventory AS target "
                           "USING (VALUES (?, ?)) AS source (Prod_ID, Inv) "
                           "ON target.Prod_ID = source.Prod_ID "
                           "WHEN MATCHED THEN "
                           "UPDATE SET target.Inv = source.Inv "
                           "WHEN NOT MATCHED THEN "
                           "INSERT (Prod_ID, Inv) VALUES (source.Prod_ID, source.Inv);",
                           (product.ID, inventory))
            connection.commit()

            return redirect(url_for('products.view_product', product_id=product.ID))

    return render_template('products/edit_product.html', product=product, categories=categories, inventory=inventory)
