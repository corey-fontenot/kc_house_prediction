import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from config import Config


def generate_rf_model():
    data = Config.HOUSE_DATA

    x = data.drop('price', axis=1)
    y = data['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    rf = RandomForestRegressor()
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)
    score = r2_score(y_test, y_pred)
    rf.score = score
    rf.mean_absolute_error = mean_absolute_error(y_test, y_pred)
    rf.mean_squared_error = mean_squared_error(y_test, y_pred)

    return rf
