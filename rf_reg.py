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
