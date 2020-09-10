from app.models import User, DataModel, HouseData
from app import db
import datetime
import csv
from pca import generate_pca_model
from rf_reg import generate_rf_model

admin_user = User.query.filter_by(username='admin').first()

if admin_user is None:
    admin_user = User()
    admin_user.username = 'admin'
    admin_user.set_password('admin')
    admin_user.create_on = datetime.date
    admin_user.last_login = datetime.datetime.now
    admin_user.is_admin = True

    db.session.add(admin_user)
    db.session.commit()

with open('cleaned_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        entry = HouseData()
        entry.price = row[0]
        entry.bedrooms = row[1]
        entry.bathrooms = row[2]
        entry.floors = row[3]
        entry.waterfront = True if int(row[4]) == 1 else False
        entry.view = True if int(row[5]) == 1 else False
        entry.zipcode = row[6]

        db.session.add(entry)
        db.session.commit()

pca_model = DataModel.query.filter_by(name='pca').first()

if pca_model is None:
    model = generate_pca_model()

    pca_model = DataModel()
    pca_model.name = 'pca'
    pca_model.model = model

    db.session.add(pca_model)
    db.session.commit()

rf_reg_model = DataModel.query.filter_by(name='rf_regression').first()

if rf_reg_model is None:
    model = generate_rf_model()

    rf_model = DataModel()
    rf_model.name = 'rf_regression'
    rf_model.model = model

    db.session.add(rf_model)
    db.session.commit()