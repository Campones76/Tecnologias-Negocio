from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, session
from network.DBSTUFF import connection_string
import re
import pyodbc

signup_bp = Blueprint('SignupView', __name__)
bcrypt = Bcrypt()
@signup_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fullname = request.form['fullname']
        address = request.form['address']
        contact = request.form['contact']
        countrycode = request.form['countryCode']
        tin = request.form['tin']
        Admin = 0
        Deactivated = 0
        full_number = '+' + countrycode + contact
        print(full_number)
        print(full_number)
        print(full_number)

        # #Date conversion
        # # Assume date_str is the date you got from the form in 'DD/MM/YY' format
        # date_str = dob
        # # Convert date_str from 'DD/MM/YY' to 'YYYY-MM-DD'
        # date_obj = datetime.strptime(date_str, '%d/%m/%y')
        # formatted_date = datetime.strftime(date_obj, '%Y-%m-%d')



        # Check if account exists using MSSQL
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dbo.[User] WHERE Username = ?', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not fullname or not address or not contact or not tin:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            #cursor.execute('INSERT INTO dbo.Admin VALUES (?, ?, ?, ?)', (username, password, email, staff,))
            # Hash the password before storing it
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute('INSERT INTO dbo.[User] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (username, fullname, email, hashed_password, full_number, tin, address, Admin, Deactivated))
            #cursor.execute('INSERT INTO dbo.Admin VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (username, password, email, fullname, dob, address, contact, tin, staff,))
            cursor.commit()
            conn.close()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)