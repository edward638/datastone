from flask import Flask, render_template
# from flask_bootstrap import Bootstrap

# def create_app():
#     app = Flask(__name__)
#     Bootstrap(app)
#     return app


app = Flask(__name__)


@app.route('/')
def base():
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


if __name__ == '__main__':
    app.run()
