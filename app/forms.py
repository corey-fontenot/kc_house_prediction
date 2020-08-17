from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User
from config import Config


class LoginForm(FlaskForm):
    # define form fields
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    # define form fields
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # custom validator to check if username already exists in the database
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken')


def integer_check(form, field):
    if not isinstance(field.data, int):
        raise ValidationError(field.label + " must be an integer")


class EstimateForm(FlaskForm):

    # define form fields
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired(), integer_check])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired(), integer_check])
    floors = IntegerField('Floors', validators=[DataRequired()])
    waterfront = BooleanField('Waterfront')
    view = BooleanField('View')
    zipcode = SelectField('Zipcode', choices=Config.ZIPCODES)
    submit = SubmitField("Estimate Price")


