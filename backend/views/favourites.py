from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import current_user, login_required
from network.DBSTUFF import connection_string
import pyodbc

favourites_bp = Blueprint('favourites', __name__)

@favourites_bp.route('/toggle_favourite', methods=['POST'])
@login_required
def toggle_favourite():
    user_id = current_user.id
    product_id = request.form.get('product_id')

    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Check if the product is already in the favourites
        cursor.execute('SELECT * FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?', (user_id, product_id))
        existing_favorite = cursor.fetchone()

        if existing_favorite:
            # Product is already in favourites, so remove it
            cursor.execute('DELETE FROM dbo.Favorites WHERE User_ID = ? AND Prod_ID = ?', (user_id, product_id))
            message = 'Product removed from favourites.'
            new_state = False
        else:
            # Product is not in favourites, so add it
            cursor.execute('INSERT INTO dbo.Favorites (User_ID, Prod_ID) VALUES (?, ?)', (user_id, product_id))
            message = 'Product added to favourites!'
            new_state = True
        conn.commit()
    referrer = request.form.get('referrer', '')

    if referrer == 'view_favourites':
        # Redirect to the favourites page
        return redirect(url_for('favourites.view_favourites'))
    else:
        # Redirect to the product page
        return redirect(url_for('products.view_product', product_id=product_id))

    # Redirect to the same page to show the updated favorite state
    #return redirect(url_for('products.view_product', product_id=product_id))

@favourites_bp.route('/view', defaults={'page': 1})
@favourites_bp.route('/view/<int:page>')
@login_required
def view_favourites(page):
    user_id = current_user.id
    items_per_page = 3
    offset = (page - 1) * items_per_page

    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        # Get the total count of favorite items for pagination
        cursor.execute('SELECT COUNT(*) FROM dbo.Favorites WHERE User_ID = ?', (user_id,))
        total_count = cursor.fetchone()[0]

        # Get a page of favorite items
        cursor.execute('''
            SELECT Product.ID, Product.Name, Product.Price
            FROM dbo.Favorites
            INNER JOIN Product ON dbo.Favorites.Prod_ID = Product.ID
            WHERE dbo.Favorites.User_ID = ?
            ORDER BY Product.Name
            OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        ''', (user_id, offset, items_per_page))
        favourites = cursor.fetchall()

    # Calculate total pages and current page range
    total_pages = (total_count + items_per_page - 1) // items_per_page

    return render_template('view_favourites.html', favourites=favourites,
                           current_page=page, total_pages=total_pages)