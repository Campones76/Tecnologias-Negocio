from flask import Blueprint, render_template
from flask_login import current_user, login_required
from network.DBSTUFF import connection_string   
import pyodbc

# Create a function to get a database connection
def get_db():
    return pyodbc.connect(connection_string)

producthistory_bp = Blueprint('PH', __name__)
@producthistory_bp.route('/purchase_history')
@login_required
def purchase_history():
    with get_db() as connection:
        cursor = connection.cursor()
        user_id = current_user.id  # Assuming you have the current user's ID

        # Query to fetch purchase history for the current user
        cursor.execute("""
            SELECT Purchase_ID, Order_Status, User_Address, Cart_ID
            FROM Purchase_History
            WHERE User_ID = ?
            ORDER BY Purchase_ID DESC
            """, (user_id,))
        purchases = cursor.fetchall()

    return render_template('purchase_history.html', purchases=purchases)
