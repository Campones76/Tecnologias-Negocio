from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from network.DBSTUFF import connection_string
import pyodbc

# Establish a database connection
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Fetch the records from the database
cursor.execute("SELECT FirearmID, Maker_Model FROM Firearms WHERE Bought = 0")
firearms = cursor.fetchall()

# Create a list of tuples for the select field choices
firearm_choices = [(firearm.FirearmID, firearm.Maker_Model) for firearm in firearms]

class FirearmForm(FlaskForm):
    firearm = SelectField('Firearm', choices=firearm_choices, validators=[DataRequired()])
    submit = SubmitField('Select')
