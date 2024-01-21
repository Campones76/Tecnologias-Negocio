from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

StaffInventoryView_bp = Blueprint('InventoryView', __name__)

@StaffInventoryView_bp.route('/InventoryView')
def inventoryview():
    if not current_user.is_authenticated or not current_user.Admin:
        return redirect(url_for('home.index'))
    return render_template('StaffInventoryView.html')