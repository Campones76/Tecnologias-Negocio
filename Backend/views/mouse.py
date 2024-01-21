# backend/views/home.py
from flask import Blueprint, render_template
from flask_login import current_user

mouse_bp = Blueprint('mouse', __name__)

@mouse_bp.route('/mouse')
def index():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    return render_template('ratos.html')