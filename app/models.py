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
    teamname = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
