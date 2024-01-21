from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional, DataRequired, Email
import pyodbc

class UpdateUserInfoForm(FlaskForm):
    username = StringField('Username', validators=[Optional()])
    nif = StringField('NIF', validators=[Optional()])
    email = StringField('New Email', validators=[Optional(), Email()])
    submit = SubmitField('Update')
