import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from config import Config


def generate_rf_model():
    data = Config.HOUSE_DATA

    x = data.drop('price', axis=1)
    y = data['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    rf = RandomForestRegressor()
    rf.fit(x_train, y_train)

    return rf

# x = data.drop('price', axis=1)
# y = data['price']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#
# rf = RandomForestRegressor()
# rf.fit(x_train, y_train)
#
# y_pred = rf.predict(x_test)
#
# fig, ax = plt.subplots(figsize=(12, 8))
# plt.scatter(y_test, y_pred)
# plt.savefig("app/static/img/rf_reg_scatter.png")
#
# df_pred_actual = pd.DataFrame({'predicted': y_pred, 'actual': y_test})
#
# df_pred_actual_sample = df_pred_actual.sample(100)
# df_pred_actual_sample = df_pred_actual_sample.reset_index()
#
# plt.figure(figsize=(20,10))
# plt.plot(df_pred_actual_sample['predicted'], label='Predicted')
# plt.plot(df_pred_actual_sample['actual'], label='Actual')
# plt.ylabel('Price')
# plt.legend()
# plt.savefig("app/static/img/rf_pred_actual")
#
# filename = "rf_reg.pkl"
# with open(filename, 'wb') as file:
#     pickle.dump(rf, file)
