from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import PasswordInput

class AddUserForm(FlaskForm):
    """Form for adding users."""

    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])

class LoginForm(FlaskForm):
    """Login Form"""

    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])