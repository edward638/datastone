from app import app, db
from app.models import Player, User
from flask import render_template, flash, redirect
from app.forms import LoginForm, DraftForm


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