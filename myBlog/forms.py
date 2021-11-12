from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, URL
from wtforms.widgets.core import SubmitInput

class registerForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(2,10)])
    password = PasswordField('Password',validators=[DataRequired(),Length(6,20)])
    submit = SubmitField('Submit')