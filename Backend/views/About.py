# backend/views/home.py
from flask import Blueprint, render_template

about_bp = Blueprint('About', __name__)

@about_bp.route('/about_us')
def index():
    return render_template('About_us.html')