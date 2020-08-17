import pandas as pd


def preprocess_data(data):
    data.dropna()
    data['date'] = data['date'].apply(pd.to_datetime).astype('int64')

    return data


# Returns preprocessed pandas data frame
def get_housing_data():
    data = pd.read_csv('kc_house_data.csv')
    housing_data = preprocess_data(data)

    return housing_data
