from flask import render_template,redirect,url_for, request
from application import app, db, Bcrypt
from application.forms import PostForm, RegistrationForm, LoginForm,UpdateAccountForm
from application.model import Posts, Users
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='Eurovision')

@app.route('/favorites', methods=[ 'GET','POST'])
@login_required
def favorites():
    form = PostForm()
    if form.validate_on_submit():
       PostData = Posts(
                country=form.country.data,
                year=form.year.data,
                performer=form.performer.data,
                song=form.song.data
            )
       db.session.add(PostData)
       db.session.commit()
    else:
       print(form.errors)
       return render_template('favorites.html', title='Eurovision Favorite Entries', form=form)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about'))

    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('about'))

    return render_template('login.html', title='Login', form=form)

@app.route('/signup')
def signup():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash
        user = Users(first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_pw)
        db.session.add(user)
        db.session.commit
        return redirect(url_for('favorites'))
    return render_template('signup.html',title='Sign Up', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    return render_template('account.html',title='Account',form=form)

