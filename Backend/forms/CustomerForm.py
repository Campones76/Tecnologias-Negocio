from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from network.DBSTUFF import connection_string
import pyodbc

class UserForm(FlaskForm):
    user = SelectField('User', validators=[DataRequired()])
    submit = SubmitField('Select')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, UserName FROM Customer WHERE Staff = 0 AND Deactivated = 0")
        users = cursor.fetchall()
        self.user.choices = [(user.CustomerID, user.UserName) for user in users]

