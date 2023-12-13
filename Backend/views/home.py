# backend/views/home.py
from flask import Blueprint, render_template
import os

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return render_template('index.html')