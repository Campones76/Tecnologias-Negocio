from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

StaffPanel_bp = Blueprint('StaffPanel', __name__)

@StaffPanel_bp.route('/StaffPanel')
def staffpanel():
    if not current_user.is_authenticated or not current_user.Admin:
        return redirect(url_for('home.index'))
    return render_template('StaffPanel.html')