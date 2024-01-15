# backend/views/home.py
from flask import Blueprint, render_template

computers_bp = Blueprint('computers', __name__)

@computers_bp.route('/computers')
def index():
    return render_template('computadores.php')