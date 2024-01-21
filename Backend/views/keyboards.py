# backend/views/home.py
from flask import Blueprint, render_template
from flask_login import current_user

keyboards_bp = Blueprint('keyboards', __name__)

@keyboards_bp.route('/keyboards')
def index():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    return render_template('teclados.html')