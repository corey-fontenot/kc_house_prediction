import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("kc_house_data.csv")

data.dropna()

data['date'] = data['date'].apply(pd.to_datetime).astype('int64')
data = data.drop('id', axis=1)

data_corr = data.corr()

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(data_corr, annot=True)

plt.savefig("app/static/img/heatmap.png")