from app import db, login
from flask_login import UserMixin

# class User(db.Model):
#     AGENT_CODE = db.Column(db.String(6), primary_key=True)
#     AGENT_NAME = db.Column(db.String(40))
#     WORKING_AREA = db.Column(db.String(35))
#     COMMISSION = db.Column(db.Float(10))
#     PHONE_NO = db.Column(db.String(15))
#     COUNTRY = db.Column(db.String(25))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True)
    cum_score = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.team_name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class PlayerData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    goals_avg = db.Column(db.REAL)
    goals_sd = db.Column(db.REAL)
    assists_avg = db.Column(db.REAL)
    assists_sd = db.Column(db.REAL)
    blocks_avg = db.Column(db.REAL)
    blocks_sd = db.Column(db.REAL)
    catches_avg = db.Column(db.REAL)
    catches_sd = db.Column(db.REAL)
    completions_avg = db.Column(db.REAL)
    completions_sd = db.Column(db.REAL)
    throwaways_avg = db.Column(db.REAL)
    throwaways_sd = db.Column(db.REAL)
    drops_avg = db.Column(db.REAL)
    drops_sd = db.Column(db.REAL)
    callahans_avg = db.Column(db.REAL)
    callahans_sd = db.Column(db.REAL)

    def __repr__(self):
        return '<PlayerData {}>'.format(self.name)

class PlayerStatus(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score_avg = db.Column(db.REAL)
    score_sd = db.Column(db.REAL)
    user_id = db.Column(db.Integer)
    active = db.Column(db.Integer)

    def __repr__(self):
        return '<PlayerStatus {}>'.format(self.name)

class Settings(db.Model):
    active = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Settings {}>'.format(self.week_number)

class Week(db.Model):
    week_number = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Week {}>'.format(self.week_number)
