from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
@app.route('/prediction')
def index():
    return render_template('base.html')


@app.route('/dashboard')
def dashboard():
    return "Dashboard page"


@app.route('/login')
def login():
    return "Login page"


@app.route('/register')
def register():
    return "Register page"


@app.route('/logout')
def logout():
    return "Logout page"
