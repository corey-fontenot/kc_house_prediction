from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_on = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, default='False', nullable=False)
    estimates = db.relationship('Estimate', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    floors = db.Column(db.Integer, nullable=False)
    zipcode = db.Column(db.String, nullable=False)
    waterfront = db.Column(db.Boolean, nullable=False)
    view = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Integer, nullable=False)


class DataModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, nullable=False)
    model = db.Column(db.PickleType, nullable=False)