from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
	username = StringField("username", validators=[InputRequired("Please enter your username"),Length(min=6, max=15)])
	password = PasswordField("password", validators=[InputRequired("Please enter your password"), Length(min=8, max=20)])
	submit = SubmitField("Login")

class RegisterForm(FlaskForm):
	email = StringField("email", validators=[InputRequired("Please enter your email"),Length(min=5, max=40)])
	username = StringField("username", validators=[InputRequired("Please enter your username"),Length(min=6, max=15)])
	password = PasswordField("password", validators=[InputRequired("Please enter your password"), Length(min=8, max=20)])
	confirm_password = PasswordField("confirm_password", validators=[InputRequired("Please enter your confirm password"), Length(min=8, max=20)])
	submit = SubmitField("Register")