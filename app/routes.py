from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@app.route('/prediction')
def index():
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    # if user is already logged in they are redirected to the dashboard page
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()

    # if form data is valid and username/password are correct the user is logged in
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)

        # sets page to load after being logged in
        next_page = request.args.get('next')

        # Sets page to dashboard if a page is not specified or url is not relative
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        flash('You have successfully logged in')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registration successful for user {}'.format(form.username.data))
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


# logs user out then redirects to the login page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
