from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    '''
    RegistrationForm class that passes in the required and email validators
    '''
    email=StringField('Email Address',validators=[Required(),Email()])
    username=StringField('Create Username',validators=[Required()])
    password=PasswordField("Password",validators=[Required(),
    EqualTo('Password',message='Passwords Must Match')])
    password_confirm=PasswordField('Confirm password',validators=[Required()])
    submit=SubmitField('Sign Up')


    #custom validators
    def validate_email(self,data_field):
        '''
        Functions takes in the data field and checks our database to confirm user Validation
        '''
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('there is an account with a similar email address')

    def validate_username(self,data_field):
        '''
        Function checks if the username is unique and raises ValidationError
        '''
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is taken. Please Choose Another.')

# LOgin form that has 3 fields
class LoginForm(FlaskForm):
    email=StringField('Email Address',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit=SubmitField('Sign in')
