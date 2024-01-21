# backend/views/home.py
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

computers_bp = Blueprint('computers', __name__)

@computers_bp.route('/computers')
def index():
    if not current_user.is_authenticated:
        return render_template('Aviso_Login.html')
    return render_template('computers.html')