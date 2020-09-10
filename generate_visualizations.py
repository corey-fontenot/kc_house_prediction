import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import Config
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = Config.HOUSE_DATA

data_corr = data.corr()

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(data_corr, annot=True)

plt.savefig("app/static/img/heatmap.png")

pca = PCA(n_components=2)

scaler = StandardScaler()
scaler.fit(data)

scaled_data = scaler.transform(data)

pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=data['price'], cmap='rainbow')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

plt.savefig("app/static/img/pca.png")

x = data.drop('price', axis=1)
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

rf = RandomForestRegressor()
rf.fit(x_train, y_train)

x = data.drop('price', axis=1)
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

rf = RandomForestRegressor()
rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)

fig, ax = plt.subplots(figsize=(12, 8))
plt.scatter(y_test, y_pred)
plt.savefig("app/static/img/rf_reg_scatter.png")

df_pred_actual = pd.DataFrame({'predicted': y_pred, 'actual': y_test})

df_pred_actual_sample = df_pred_actual.sample(100)
df_pred_actual_sample = df_pred_actual_sample.reset_index()

plt.figure(figsize=(20,10))
plt.plot(df_pred_actual_sample['predicted'], label='Predicted')
plt.plot(df_pred_actual_sample['actual'], label='Actual')
plt.ylabel('Price')
plt.legend()
plt.savefig("app/static/img/rf_pred_actual")
