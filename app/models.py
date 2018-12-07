from app import db, login
from sqlalchemy import sql, orm
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
    @staticmethod
    def setActive(player_id, active_value):
        try:
            db.session.execute('UPDATE player_status SET active = :active_value'
                               ' WHERE player_id = :player_id',
                               dict(player_id=player_id, active_value=active_value))
            db.session.commit()

        except Exception as e:
            print("update failed")
            db.session.rollback()
            raise e

    @staticmethod
    def reset():
        try:
            db.session.execute('UPDATE player_status SET user_id = -1, active = 0')
            db.session.commit()

        except Exception as e:
            print("reset failed")
            db.session.rollback()
            raise e

    def __repr__(self):
        return '<PlayerStatus {}>'.format(self.name)

class PlayerWeeklyStats(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, primary_key=True)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    catches = db.Column(db.Integer)
    completions = db.Column(db.Integer)
    throwaways = db.Column(db.Integer)
    drops = db.Column(db.Integer)
    callahans = db.Column(db.Integer)
    score = db.Column(db.REAL)

    @staticmethod
    def populate(week):
        try:
            # print("hi")
            db.session.execute('WITH IND(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM player_status) - 1, 1))'
		'INSERT INTO player_weekly_stats SELECT '
			'i,'
			 ':week,'
			 '(SELECT (ROUND(goals_avg+goals_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(assists_avg+assists_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(blocks_avg+blocks_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(catches_avg+catches_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(completions_avg+completions_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(throwaways_avg+throwaways_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(drops_avg+drops_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '(SELECT (ROUND(callahans_avg+callahans_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),'
			 '0'
             ' FROM IND', dict(week=week))
            db.session.commit()

        except Exception as e:
            print("populate failed")
            db.session.rollback()
            raise e

    @staticmethod
    def remove_negatives():
        try:
            db.session.execute('UPDATE player_weekly_stats SET goals = 0 WHERE goals < 0')
            db.session.execute('UPDATE player_weekly_stats SET assists = 0 WHERE assists < 0')
            db.session.execute('UPDATE player_weekly_stats SET blocks = 0 WHERE blocks < 0')
            db.session.execute('UPDATE player_weekly_stats SET catches = 0 WHERE catches < 0')
            db.session.execute('UPDATE player_weekly_stats SET completions = 0 WHERE completions < 0')
            db.session.execute('UPDATE player_weekly_stats SET drops = 0 WHERE drops < 0')
            db.session.execute('UPDATE player_weekly_stats SET throwaways = 0 WHERE throwaways < 0')
            db.session.execute('UPDATE player_weekly_stats SET callahans = 0 WHERE callahans < 0')

            db.session.execute('UPDATE player_weekly_stats as t set score = (12*t.goals+12*t.assists+24*t.blocks+0.5*t.catches+0.5*t.completions-14*t.throwaways-14*t.drops+72*t.callahans)'
            ' from player_weekly_stats as c'
            ' where c.player_id = t.player_id')



            db.session.commit()



        except Exception as e:
            print("remove negatives failed")
            db.session.rollback()
            raise e

    @staticmethod
    def reset():
        try:
            db.session.execute('DELETE FROM player_weekly_stats')
            db.session.commit()

        except Exception as e:
            print("reset failed")
            db.session.rollback()
            raise e

class Settings(db.Model):
    active = db.Column(db.Integer, primary_key=True)

    @staticmethod
    def reset():
        try:
            db.session.execute('UPDATE settings SET active = 0')
            db.session.commit()

        except Exception as e:
            print("reset failed")
            db.session.rollback()
            raise e

    def __repr__(self):
        return '<Settings {}>'.format(self.week_number)

class Week(db.Model):
    week_number = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Week {}>'.format(self.week_number)


