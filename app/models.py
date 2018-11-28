from app import db


# class User(db.Model):
#     AGENT_CODE = db.Column(db.String(6), primary_key=True)
#     AGENT_NAME = db.Column(db.String(40))
#     WORKING_AREA = db.Column(db.String(35))
#     COMMISSION = db.Column(db.Float(10))
#     PHONE_NO = db.Column(db.String(15))
#     COUNTRY = db.Column(db.String(25))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.team_name)


# class Player(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     goals_average = db.Column(db.Float)
#     goals_lambda = db.Column(db.Float)
#     assists_average = db.Column(db.Float)
#     blocks_average = db.Column(db.Float)
#     catches_average = db.Column(db.Float)
#     completions_average = db.Column(db.Float)
#     throwaways_average = db.Column(db.Float)
#     drops_average = db.Column(db.Float)
#     score_average = db.Column(db.Float)
#     taken = db.Column(db.Boolean)
#
#     def __repr__(self):
#         return '<Player {}>'.format(self.name)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(64))
    goals = db.Column(db.REAL)
    assists = db.Column(db.REAL)
    blocks = db.Column(db.REAL)
    catches = db.Column(db.REAL)
    completions = db.Column(db.REAL)
    throwaways = db.Column(db.REAL)
    drops = db.Column(db.REAL)
    callahans = db.Column(db.REAL)

    def __repr__(self):
        return '<Player {}>'.format(self.name)


class Performs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, primary_key=True)
    callahans = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    drops = db.Column(db.Integer)
    catches = db.Column(db.Integer)
    completions = db.Column(db.Integer)
    throwaways = db.Column(db.Integer)

    def __repr__(self):
        return '<Performs {}>'.format(self.week_number)


class Week(db.Model):
    week_number = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Week {}>'.format(self.week_number)
