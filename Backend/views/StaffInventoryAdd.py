from flask import Blueprint, current_app, flash, redirect, request, render_template, redirect, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename
import os
from network.DBSTUFF import connection_string
import pyodbc

StaffInventory_bp = Blueprint('Inventory_bp', __name__)



# Assuming you have already configured your database connection
conn = pyodbc.connect(connection_string)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@StaffInventory_bp.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if not current_user.is_authenticated or not current_user.Admin:
        return redirect(url_for('home.index')) 
    if request.method == 'POST':
        product_name = request.form['productName']
        #product_description = request.form['productDescription']
        product_price = request.form['productPrice']
        cover_image = request.files['coverImage']

        if cover_image and allowed_file(cover_image.filename):
            filename = secure_filename(cover_image.filename)
            # Note the use of current_app here
            cover_image.save(os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], filename))
            
            # Add the product information to the database
            # (Ensure you establish a database connection properly here)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Product (Name, Price, CoverImagePath) 
                VALUES (?, ?, ?)
                """, (product_name, product_price, filename))
            conn.commit()
            cursor.close()
            flash('Product successfully added', 'success')
            return redirect(url_for('Inventory_bp.add_product'))
        else:
            flash('Allowed file types are png, jpg, jpeg, gif', 'error')

    return render_template('StaffInventoryAdd.html')

@StaffInventory_bp.route('/product-list')
def product_list():
    # Fetch and display products
    return render_template('product_list.html')

@StaffInventory_bp.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('path_to_save', filename))
        # Save the path in the database
    return 'Image uploaded successfully'