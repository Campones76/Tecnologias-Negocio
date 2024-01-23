from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from network.DBSTUFF import connection_string
import pyodbc
from backend.forms.UpdateUserInfoForm import UpdateUserInfoForm

accountupdate_bp = Blueprint('AccountUpdate', __name__)

@accountupdate_bp.route('/update_info', methods=['GET', 'POST'])
@login_required
def update_info():
    form = UpdateUserInfoForm()
    # Check if the current user is an admin
    if current_user.Admin:
        return 'Admins are not allowed to update their information.'
    
    if form.validate_on_submit():
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Create a list of columns to update based on what fields have been filled out
        updates = []
        params = []
        if form.username.data:
            updates.append("Username = ?")
            params.append(form.username.data)
        if form.nif.data:
            updates.append("NIF = ?")
            params.append(form.nif.data)
        if form.email.data:
            updates.append("Email = ?")
            params.append(form.email.data)

        # Construct the SQL statement
        sql = "UPDATE [User] SET " + ", ".join(updates) + " WHERE ID = ?;"
        params.append(current_user.id)
        
        # Execute the update query safely with parameters
        cursor.execute(sql, params)
        conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()
        
        flash('Your information has been updated.', 'success')
        return redirect(url_for('AccountStateView.accountstate'))  # Replace 'profile' with the correct route for your profile page
    
    return render_template('update_info.html', title='Update Information', form=form)