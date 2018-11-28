from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

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
