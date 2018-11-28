from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

# app.secret_key = 'datastone bois'
# app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
@app.route('/index')
def base():
    # return "sup bois"
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # if user is None or not user.check_password(form.password.data):
        if user is None:
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/profile/<name>')
def user_welcome(name):
    return render_template("user.html", name=name)

@app.route('/standings')
def standings():
    return render_template("standings.html")

@app.route('/draft')
def draft():
    return render_template("draft.html")

@app.route('/draft/start')
def draft_start():
    return render_template("draft_start.html")
