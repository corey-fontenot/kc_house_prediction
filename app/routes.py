from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegisterForm, EstimateForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Estimate
from werkzeug.urls import url_parse
import datetime
import pickle


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = EstimateForm(request.form)

    if form.validate_on_submit():
        filename = "rf_reg.pkl"
        input_data = [
            [
                form.bedrooms.data,
                form.bathrooms.data,
                form.floors.data,
                form.waterfront.data,
                form.view.data,
                form.zipcode.data
            ]
        ]
        with open(filename, 'rb') as file:
            rf_reg_model = pickle.load(file)
            result = rf_reg_model.predict(input_data)

        result = {
            'bedrooms': form.bedrooms.data,
            'bathrooms': form.bathrooms.data,
            'floors': form.floors.data,
            'waterfront': form.waterfront.data,
            'view': form.view.data,
            'zipcode': form.zipcode.data,
            'price': "${:}".format(int(result[0]))
        }
        return render_template('results.html', title="Results", result=result)

    return render_template('index.html', title="Home Price Estimator", form=form)


@app.route('/results/<estimate_id>')
@login_required
def results(estimate_id):

    result = Estimate.query.filter_by(id=estimate_id).first()

    return render_template('results.html', result=result)


@app.route('/dashboard')
@login_required
def dashboard():
    estimates = Estimate.query.filter_by(user_id=current_user.id)
    return render_template('dashboard.html', estimates=estimates)


@app.route('/login', methods=['GET', 'POST'])
def login():

    # if user is already logged in they are redirected to the estimates page
    if current_user.is_authenticated:
        return redirect(url_for('estimates'))
    form = LoginForm()

    # if form data is valid and username/password are correct the user is logged in
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login', error=True))
        login_user(user)

        # update last_login column for user
        current_user.last_login = str(datetime.datetime.now())
        db.session.commit()

        # sets page to load after being logged in
        next_page = request.args.get('next')

        # Sets page to dashboard if a page is not specified or url is not relative
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('estimates')
        flash('You have successfully logged in')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    # if user is already logged in, redirect them to the dashboard page
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegisterForm()

    # if form validates, create new user and insert into the database
    if form.validate_on_submit():
        cur_date = str(datetime.datetime.now())
        user = User()
        user.username = form.username.data
        user.created_on = cur_date
        user.last_login = cur_date
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful for user {}'.format(form.username.data))

        # redirect to the login page so new user can log in
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


# logs user out then redirects to the login page
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for('login'))


@app.route('/save_estimate', methods=['GET', 'POST'])
def save_estimate():

    estimate = Estimate()
    estimate.date = datetime.date.today()
    estimate.user_id = current_user.id
    estimate.bedrooms = request.args.get('bedrooms')
    estimate.bathrooms = request.args.get('bathrooms')
    estimate.floors = request.args.get('floors')
    estimate.zipcode = request.args.get('zipcode')
    estimate.view = True if request.args.get('view') == 'True' else False
    estimate.waterfront = True if request.args.get('waterfront') == 'True' else False
    estimate.price = int(request.args.get('price')[1:])

    db.session.add(estimate)
    db.session.commit()

    flash("Your estimate has been saved")

    return redirect(url_for('estimates'))


@app.route('/estimates')
@login_required
def estimates():
    user_estimates = Estimate.query.filter_by(user_id=current_user.id)
    return render_template('estimates.html', estimates=user_estimates)
