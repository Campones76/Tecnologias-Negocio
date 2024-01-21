from flask import Blueprint, Flask, render_template
from flask_login import current_user
from network.DBSTUFF import connection_string
import pyodbc

carrinho_bp = Blueprint('carrinho', __name__)

@carrinho_bp.route('/carrinho')
def shopping_cart():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    
    # Connection string
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Update your SQL query here
    #query = "SELECT id, name, quantity, price FROM products"  # Modify query based on your database schema
    #cursor.execute(query)
    #products = cursor.fetchall()

    cursor.close()
    conn.close()

    #return render_template('carrinho_compras.html', products=products)
    return render_template('carrinho_compras.html')
