from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

# app.secret_key = 'datastone bois'
# app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
@app.route('/index')
def base():
    # return "sup bois"
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', form=form)

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