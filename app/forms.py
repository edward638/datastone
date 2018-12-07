from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DraftForm(FlaskForm):
    # player_id = SelectField(u'Player', validators=[DataRequired()], coerce=int)
    # user_id = SelectField(u'User', validators=[DataRequired()], coerce=int)
    player_id = SelectField(u'Player', coerce=int)
    user_id = SelectField(u'User', coerce=int)
    submit = SubmitField('Choose')

class StartDraftForm(FlaskForm):
    submit = SubmitField('Start')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')

class ResetForm(FlaskForm):
    submit = SubmitField('Reset Season')

class ResetAllForm(FlaskForm):
    submit = SubmitField('Reset Season and Users')
