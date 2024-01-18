# backend/views/home.py
from flask import Blueprint, render_template

mouse_bp = Blueprint('mouse', __name__)

@mouse_bp.route('/mouse')
def index():
    return render_template('ratos.html')