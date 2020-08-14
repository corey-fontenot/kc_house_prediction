from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
@app.route('/prediction')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/logout')
def logout():
    return "Logout page"
