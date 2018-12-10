from app import app, db

from app.models import PlayerStatus, User, Settings, PlayerWeeklyStats, Week, PlayerActive
from app.forms import LoginForm, DraftForm, RegistrationForm, StartDraftForm, ResetForm, ResetAllForm, IterateWeekForm, ChooseWeekForm, ChooseTeamForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

# app.secret_key = 'datastone bois'
# app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
@app.route('/index')
def base():
    # return "sup bois"
    reset = ResetForm()
    reset_all = ResetAllForm()
    iterate = IterateWeekForm()
    settings = Settings.query.all()
    is_active = [x.active for x in settings][0]
    week = Week.query.all()
    week_number = [x.week_number for x in week][0]
    return render_template("index.html", reset=reset, reset_all=reset_all, is_active=is_active, iterate=iterate, week_number=week_number)

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

@app.route('/profile', methods=['GET','POST'])
def user_welcome():
    if current_user.is_authenticated:
        error = ""
        players = PlayerStatus.query.all()
        player_list = [[i.player_id, i.name, i.active] for i in players if i.user_id == current_user.id]

        if request.method == 'POST':
            values = request.form.getlist("active")
            if len(values) > 7:
                error = "You can only select up to 7 players."
                return render_template("user.html", player_list=player_list, error=error)
            for player in player_list:
                PlayerStatus.setActive(int(player[0]), 0)
            for i in values:
                PlayerStatus.setActive(int(i), 1)

            players = PlayerStatus.query.all()
            player_list = [[i.player_id, i.name, i.active] for i in players if i.user_id == current_user.id]

        return render_template("user.html", player_list=player_list, error=error)
    else:
        return render_template("user_default.html")


@app.route('/standings')
def standings():
    week1 = Week.query.all()
    week_number = [x.week_number for x in week1][0]
    results = PlayerActive.get_standings(week_number)
    rows = []
    for x in results:
        row = []
        for i in x:
            # print(i)
            row.append(i)
        rows.append(row)
    return render_template("standings.html", standings=rows, week=week_number)

@app.route('/teams', methods=['GET','POST'])
def team():
    form = ChooseTeamForm()
    users = User.query.all()
    form.choose_team.choices = [(j.id, j.username) for j in users]
    if form.submit.data and form.validate_on_submit():
        results = User.show_team(form.choose_team.data)
        rows = []
        user = User.query.filter_by(id=form.choose_team.data).first()
        user = user.username
        for x in results:
            row = []
            for i in x:
                row.append(i)
            rows.append(row)

        bench = User.show_bench(form.choose_team.data)
        rows1 = []
        for x in bench:
            row = []
            for i in x:
                row.append(i)
            rows1.append(row)

        return render_template("team.html", form=form, active=rows, bench=rows1, user=user, show=1)

    return render_template("team.html", form=form)

# @app.route('/week/<week>', methods=['GET','POST'])
# def show_week(week):
#     results = PlayerWeeklyStats.show_player_stats(week)
#     form = ChooseWeekForm()
#     week1 = Week.query.all()
#     week_number = [x.week_number for x in week1][0]
#     form.choose_week.choices = [(i, i) for i in range(1, week_number+1)]
#
#     if form.submit.data and form.validate_on_submit():
#         redirect1 = '/week/' + str(form.choose_week.data)
#         # print(redirect)
#         return redirect(redirect1)
#
#     rows = []
#     for x in results:
#         row = []
#         for i in x:
#             # print(i)
#             row.append(i)
#         rows.append(row)
#     team_results = PlayerWeeklyStats.show_team_stats(week)
#     team_rows = []
#     for x in team_results:
#         team_row = []
#         for i in x:
#             # print(i)
#             team_row.append(i)
#         team_rows.append(team_row)
#
#     return render_template("week.html", rows=rows, team_rows=team_rows, week=week, form=form)

@app.route('/week')
def week():
    return redirect('/week/1')

@app.route('/week/<week>', methods=['GET','POST'])
def show_week(week):
    results = PlayerWeeklyStats.show_player_stats(week)
    form = ChooseWeekForm()
    week1 = Week.query.all()
    week_number = [x.week_number for x in week1][0]
    form.choose_week.choices = [(i, i) for i in range(1, week_number+1)]

    if form.submit.data and form.validate_on_submit():
        redirect1 = '/week/' + str(form.choose_week.data)
        # print(redirect)
        return redirect(redirect1)

    rows = []
    for x in results:
        row = []
        for i in x:
            # print(i)
            row.append(i)
        rows.append(row)
    team_results = PlayerWeeklyStats.show_team_stats(week)
    team_rows = []
    for x in team_results:
        team_row = []
        for i in x:
            # print(i)
            team_row.append(i)
        team_rows.append(team_row)

    return render_template("week.html", rows=rows, team_rows=team_rows, week=week, form=form)

@app.route('/draft', methods=['GET', 'POST'])
def draft():
    if current_user.is_authenticated:
        start = StartDraftForm()
        form = DraftForm()
        players = PlayerStatus.query.all()
        users = User.query.all()
        user_list = [i for i in users if i.id == current_user.id]

        settings = Settings.query.all()
        is_active = [x.active for x in settings][0]
        form.player_id.choices = [(i.player_id, i.name) for i in players if i.user_id == -1]
        form.user_id.choices = [(j.id, j.username) for j in user_list]

        if start.submit.data and start.validate_on_submit() and is_active != 1:
            print("start validated")
            settings_update = Settings.query.first()
            settings_update.active = 1
            db.session.commit()

            for i in range(1, 17):
                PlayerWeeklyStats.populate(i)
            PlayerWeeklyStats.remove_negatives()

            return redirect('/draft')

        if form.validate_on_submit() and form.submit.data:
            print("form validated")
            player_update = PlayerStatus.query.filter_by(player_id=form.player_id.data).first()
            player_update.user_id = form.user_id.data
            db.session.commit()
            return redirect('/draft')

        draftees = dict()
        max = 0
        for x in users:
            draftees[x.username] = list()
            for player in PlayerStatus.query.filter_by(user_id=x.id):
                draftees[x.username].append(player.name)
            if len(draftees[x.username]) > max:
                max = len(draftees[x.username])

        return render_template("draft.html", start=start, form=form, is_active=is_active, draftees=draftees, max=max)
    else:
        return render_template("user_default.html")

@app.route('/reset', methods=['GET', 'POST'])
def reset_draft():
    settings = Settings.query.all()
    is_active = [x.active for x in settings][0]
    reset = ResetForm()
    if reset.submit.data and reset.validate_on_submit() and is_active == 1:
        print("reset validated")
        PlayerStatus.reset()
        Settings.reset()
        PlayerWeeklyStats.reset()
        Week.reset()
    return redirect('/index')

@app.route('/resetall', methods=['GET', 'POST'])
def reset_all():
    settings = Settings.query.all()
    is_active = [x.active for x in settings][0]
    reset_all = ResetAllForm()
    if reset_all.submit.data and reset_all.validate_on_submit() and is_active == 1:
        print("resetall validated")
        PlayerStatus.reset()
        Settings.reset()
        PlayerWeeklyStats.reset()
        User.delete_users()
        Week.reset()
    return redirect('/index')

@app.route('/iterate', methods=['GET', 'POST'])
def iterate_week():
    iterate = IterateWeekForm()
    if iterate.submit.data and iterate.validate_on_submit():
        Week.iterate()
        week = Week.query.all()
        week_number = [x.week_number for x in week][0]
        PlayerActive.iterate(week_number)
        print("iterated")

    return redirect('/index')

@app.route('/draft/start')
def draft_start():
    return render_template("draft_start.html")
