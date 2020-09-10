import pandas as pd

data = pd.read_csv('kc_house_data.csv')

data.dropna()

data = data.drop(columns=['id', 'date', 'sqft_living', 'sqft_lot', 'condition', 'grade', 'sqft_above', 'sqft_basement',
                          'yr_renovated', 'yr_built', 'lat', 'long', 'sqft_living15', 'sqft_lot15'], axis=1)

data.to_csv('cleaned_data.csv', index=False)