from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

StaffSalesView_bp = Blueprint('SalesView', __name__)

@StaffSalesView_bp.route('/SalesView')
def salesview():
    if not current_user.is_authenticated or not current_user.Admin:
        return redirect(url_for('home.index'))
    return render_template('StaffSalesView.html')