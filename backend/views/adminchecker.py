from flask import Blueprint, render_template

adminchecker_bp = Blueprint('adminchecker', __name__)

@adminchecker_bp.route('/adminchecker')
def check():
    return render_template('adminchecker.html')