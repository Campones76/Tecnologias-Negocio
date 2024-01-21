from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
class LicenseInfoForm(FlaskForm):
    renewal_date = DateField('Renewal Date', format='%Y-%m-%d', validators=[DataRequired()])
    expiry_date = DateField('Expiry Date', format='%Y-%m-%d', validators=[DataRequired()])
    renewal_process_records = StringField('Renewal Process Records', validators=[DataRequired()])
    submit = SubmitField('Submit')