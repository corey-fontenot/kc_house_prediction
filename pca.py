import pandas as pd
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from config import Config


def generate_pca_model():
    data = Config.HOUSE_DATA

    pca = decomposition.PCA(n_components=2)

    scaler = StandardScaler()
    scaler.fit(data)

    scaled_data = scaler.transform(data)

    pca.fit(scaled_data)

    return pca


# plt.figure(figsize=(8,6))
# plt.scatter(x_pca[:,0], x_pca[:,1], c=data['price'], cmap='rainbow')
# plt.xlabel('First Principal Component')
# plt.ylabel('Second Principal Component')
#
# plt.savefig("app/static/img/pca.png")
