from flask import Blueprint, render_template, request, session, redirect, url_for
from network.DBSTUFF import connection_string
import re
import pyodbc
from flask_bcrypt import Bcrypt

edit_bp = Blueprint('edit', __name__)
bcrypt = Bcrypt()

@edit_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    # Output message if something goes wrong...
    msg = ''
    new_username = None
    new_nif = None
    new_contacts = None
    new_email = None

    # Check if the 'user_id' key is in the session
    if 'user_id' not in session:
        msg = 'User not logged in.'
        return render_template('edit_profile.html', msg=msg)

    # Continue processing for both GET and POST requests
    if request.method == 'POST':
        # Create variables for easy access
        new_username = request.form['username']
        new_nif = request.form['nif']
        new_contacts = request.form['contacts']
        new_email = request.form['email']

        user_id = session['user_id']

        # Check if account exists using MSSQL
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Check if the new username is already taken
        cursor.execute('SELECT * FROM dbo.[User] WHERE Username = ? AND ID != ?', (new_username, user_id))
        username_taken = cursor.fetchone()

        # Check if the new NIF is already taken
        cursor.execute('SELECT * FROM dbo.[User] WHERE NIF = ? AND ID != ?', (new_nif, user_id))
        nif_taken = cursor.fetchone()

        # If account with the new username exists show error
        if username_taken:
            msg = 'Username already taken!'
        # If account with the new NIF exists show error
        elif nif_taken:
            msg = 'NIF already taken!'
        elif not re.match(r'^[A-Za-z0-9]+$', new_username):
            msg = 'Username must contain only characters and numbers!'
        elif not re.match(r'^[0-9]+$', new_nif):
            msg = 'NIF must contain only numbers!'
        else:
            # Update username, NIF, contacts, and email in accounts table
            cursor.execute('UPDATE dbo.[User] SET Username = ?, NIF = ?, Telefone = ?, Email = ? WHERE ID = ?', 
                           (new_username, new_nif, new_contacts, new_email, user_id))
            conn.commit()
            conn.close()

            # Update session with the new username
            session['username'] = new_username

            msg = 'Your username, NIF, contacts, and email are updated!'

    # Show the edit_profile.html template with the message (if any)
    return render_template('edit_profile.html', msg=msg)