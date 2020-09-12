from app.models import User, DataModel, HouseData
from app import db
import datetime
import csv
from pca import generate_pca_model
from rf_reg import generate_rf_model


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

    for row, c in reader, range(1, 8000):
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

model = generate_pca_model()

pca_model = DataModel()
pca_model.name = 'pca'
pca_model.model = model

db.session.add(pca_model)
db.session.commit()

model = generate_rf_model()

rf_model = DataModel()
rf_model.name = 'rf_regression'
rf_model.model = model

db.session.add(rf_model)
db.session.commit()
