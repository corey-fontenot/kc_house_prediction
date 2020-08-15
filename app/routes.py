from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
@app.route('/prediction')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registration successful for user {}'.format(form.username.data))
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    return "Logout page"
