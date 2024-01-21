from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from network.DBSTUFF import connection_string
import pyodbc

# Establish a database connection
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Fetch the users
cursor.execute("SELECT CustomerID, UserName, HasLicense FROM Customer WHERE Staff = 0")
usersLicense = cursor.fetchall()

# Create a list of tuples for the select field choices
choices = [(user.CustomerID, user.UserName, user.HasLicense) for user in usersLicense]

class UserForm(FlaskForm):
    user = SelectField('User', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Select')

class LicenseForm(FlaskForm):
    has_license = BooleanField('Has License')
    submit = SubmitField('Submit')
