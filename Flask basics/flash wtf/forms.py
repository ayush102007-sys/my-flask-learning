from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="Name is required")])
    email = StringField("Email", validators=[DataRequired(), Email(message="Email is invalid")])
    password = PasswordField("Password", validators=[DataRequired(message="Minimum 6 characters required"), Length(min=6)])
    submit = SubmitField("Register")
    