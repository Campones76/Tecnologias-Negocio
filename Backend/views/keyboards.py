# backend/views/home.py
from flask import Blueprint, render_template

keyboards_bp = Blueprint('keyboards', __name__)

@keyboards_bp.route('/keyboards')
def index():
    return render_template('teclados.html')