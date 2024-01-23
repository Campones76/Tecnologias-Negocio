from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user
from network.DBSTUFF import connection_string
import re
import pyodbc

accountstate_bp = Blueprint('AccountStateView', __name__)

@accountstate_bp.route('/account')
def accountstate():
    return render_template('accountstateview.html')

# create a new pyodbc connection
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@accountstate_bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    user_id = current_user.id  # assuming you have access to current_user.id

    # Check if the user is a staff member
    cursor.execute("""
        SELECT Admin FROM dbo.[User] WHERE ID = ?
    """, user_id)
    result = cursor.fetchone()
    if result is not None and result[0] == 1:
        # If the user is a staff member, do not allow account deletion
        return 'Not possible' # redirect to an error page or similar

    # pseudonymize user data
    cursor.execute("""
        UPDATE dbo.[User]
        SET Username = 'XXXXX', Name = 'XXXXX', Email = 'XXXXX@GDPRrequest.eu', Password = 'XXXXX', Telefone = 'XXXXX', Address = 'XXXXX', Deactivated = 'True'
        WHERE ID = ?
    """, user_id)
    conn.commit()
    conn.close()
    logout_user()
    return redirect(url_for('home.index'))