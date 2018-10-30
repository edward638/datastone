from app import app

from flask import render_template, session

app.secret_key = 'datastone bois'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def base():
    # return "sup bois"
    return render_template("base.html")

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