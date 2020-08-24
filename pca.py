import pandas as pd
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("kc_house_data.csv")

data.dropna()

data['date'] = data['date'].apply(pd.to_datetime).astype('int64')
data = data.drop('id', axis=1)

pca = decomposition.PCA(n_components=2)

scaler = StandardScaler()
scaler.fit(data)

scaled_data = scaler.transform(data)

pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0], x_pca[:,1], c=data['price'], cmap='rainbow')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

plt.savefig("app/static/img/pca.png")
