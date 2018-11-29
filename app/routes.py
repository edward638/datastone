from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm, DraftForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Player

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        # user = User(username=form.username.data, email=form.email.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/profile')
def user_welcome():
    return render_template("user.html")

@app.route('/standings')
def standings():
    return render_template("standings.html")

@app.route('/draft', methods=['GET', 'POST'])
def draft():
    form = DraftForm()
    players = Player.query.all()
    users = User.query.all()
    form.player_id.choices = [(i.id, i.player) for i in players if i.owner == -1]
    form.user_id.choices = [(j.id, j.team_name) for j in users]
    print(form.validate_on_submit())

    if form.validate_on_submit():
        player_update = Player.query.filter_by(id=form.player_id.data).first()
        player_update.owner = form.user_id.data
        db.session.commit()

        return redirect('/draft')

    return render_template("draft.html", form=form)

@app.route('/draft/start')
def draft_start():
    return render_template("draft_start.html")
