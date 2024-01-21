from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    purchase_invoice = StringField('Purchase Invoice', validators=[DataRequired()])
    total = DecimalField('Total', validators=[DataRequired()])
    OwnershipJustification = StringField('Ownership Justification')
    background_check_results = StringField('Background Check Results')
    waiting_period_info = StringField('Waiting Period Info')
    additional_notes = StringField('Additional Notes')
    submit = SubmitField('Submit')