from numpy.core.fromnumeric import nonzero
import pandas as pd
import numpy as np
from pandas.core.dtypes.missing import isna
from sklearn import datasets
from sklearn.datasets import load_wine
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs


wine = load_wine()
wine.feature_names


# separate the data from the target attributes
X = wine.data
y = wine.target
# normalize the data attributes
wine_stand = preprocessing.normalize(X)
print(wine_stand)

df = pd.DataFrame(data=np.c_[wine_stand['target'], wine_stand['data']], columns=['class'] + wine_stand['feature_names'])
# # print(np.count_nonzero(df))
# # print(df.isna().sum())

dbdata = df.values

# print(X)
dbscan = DBSCAN(eps=3,min_samples=2)

# #fitting the model
model = dbscan.fit(dbdata)

labels = model.labels_

print(labels)
smaple_cores = np.zeros_like(labels,dtype=bool)

smaple_cores[dbscan.core_sample_indices_]=True

n_clusters= len(set(labels))-(1 if -1 in labels else 0)

print(n_clusters)

print(metrics.silhouette_score(X,labels))

# print(smaple_cores)