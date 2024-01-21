# backend/views/home.py
from flask import Blueprint, render_template
from flask_login import current_user

displays_bp = Blueprint('displays', __name__)

@displays_bp.route('/displays')
def index():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    return render_template('monitores.html')