# backend/views/home.py
from flask import Blueprint, render_template

displays_bp = Blueprint('displays', __name__)

@displays_bp.route('/displays')
def index():
    return render_template('monitores.html')