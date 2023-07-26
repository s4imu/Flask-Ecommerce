from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_user(self, check_user):
        user = User.query.filter_by(user=check_user.data).first()
        if user:
            raise ValidationError("Username already in use! Please use another username.")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email already in use! Please use another email.")

    user = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Password Confirmation:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    user = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class BuyProductForm(FlaskForm):
    submit = SubmitField(label='Buy Product')

class SaleProductForm(FlaskForm):
    submit = SubmitField(label='Sale Product')
