from flask import Blueprint, render_template, request, session
from network.DBSTUFF import connection_string
import re
import pyodbc

edit_bp = Blueprint('edit', __name__)

@edit_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    # Output message if something goes wrong...
    msg = ''
    new_username = None  # Define new_username here

    # Check if the 'username' key is in the session
    if 'username' not in session:
        msg = 'User not logged in.'
        return render_template('edit_profile.html', msg=msg)

    # Continue processing for both GET and POST requests

    if request.method == 'POST' and 'username' in request.form:
        # Create variables for easy access
        new_username = request.form['username']

        current_username = session['username']

        # Check if account exists using MSSQL
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM dbo.[User] WHERE Username = ?', (new_username,))
        account = cursor.fetchone()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'^[A-Za-z0-9]+$', new_username):
            msg = 'Username must contain only characters and numbers!'
        else:
            # Account doesn't exist, and the form data is valid, now update username in accounts table
            cursor.execute('UPDATE dbo.[User] SET Username = ? WHERE Username = ?', (new_username, current_username))
            conn.commit()
            conn.close()

            # Update session with the new username
            session['username'] = new_username

            msg = 'Your username is updated!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'

    # Show the edit_profile.html template with the message (if any)
    return render_template('edit_profile.html', msg=msg)