import matplotlib.pyplot as plt
# from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import adjusted_rand_score
import pandas as pd
import numpy as np

wine = load_wine()
df = pd.DataFrame(data=np.c_[wine['target'], wine['data']],
                 columns=['class'] + wine['feature_names'])

# # Key aspects of the dataset
# print("Features:", wine.feature_names)
# print("Targets:", wine.target_names)
# print("Total number of values:", df['class'].count())
# print("Dimensions of the dataset:", df.shape)
# print("")
# print("Number of values for each class:\n", df.groupby('class').count())
# print("")

# # Summary statistics
# print("Summary Statistics:")
# print(df.describe())
# print("")

# # Check the data types for each column
# print(df.dtypes)
# print("")

# # Check for null values
# print(df.isnull().sum())
# print("")

# Preparing the dataset to be used for further machine learning
X = df.drop(['class'], axis=1)
Y = df.iloc[:, :1]
# print(Y.head())


# separate the data from the target attributes
X_data = wine.data
y = wine.target

# kmean_params = {
#     "init": "random",
#     "n_init": 10,
#     "max_iter": 300,
#     "random_state": 42,
# }

# #  SSE values for each k
# Elbowpoints = []
# for k in range(1, 10):
#     kmeans = KMeans(n_clusters=k, **kmean_params)
#     kmeans.fit(X_data)
#     Elbowpoints.append(kmeans.inertia_)

# print(Elbow)
# kmeans_silhouette = silhouette_score(X_data, kmeans.labels_)
# print(kmeans_silhouette)
# plt.style.use("fivethirtyeight")
# plt.plot(range(1, 10), Elbowpoints)
# plt.xticks(range(1, 10))
# plt.xlabel("Cluster Numbers")
# plt.ylabel("SSE")
# plt.show()


#=================================================================

#  Instantiate k-means and dbscan algorithms
kmeans = KMeans(n_clusters=3,random_state= 42)
dbscan = DBSCAN(eps=30, min_samples=2)

# Fit the algorithms to the features
kmeans.fit(X)
dbscan.fit(X_data)

# Compute the silhouette scores for each algorithm
kmeans_silhouette = silhouette_score(X, kmeans.labels_)
dbscan_silhouette = silhouette_score(X_data, dbscan.labels_)
print(kmeans_silhouette)
print(dbscan_silhouette)

# Plot the data and cluster silhouette comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6), sharex=True, sharey=True)

fig.suptitle(f"Clustering Algorithm Comparison: Crescents", fontsize=16)
fte_colors = {
    0: "#008fd5",
    1: "#fc4f30",
    2: "#5c5c20",
    3: "#2c9f45",
    4: "#8a7967",
    5: "#d20962",
    6: "#0cb9c1",
    -1:"#000000"
}
# print(kmeans.labels_)
# # The k-means plot
km_colors = [fte_colors[label] for label in kmeans.labels_]
# ax1.scatter(X_data[:, 0], X_data[:, 1], c=km_colors)
# ax1.set_title(f"k-means\nSilhouette: {kmeans_silhouette}", fontdict={"fontsize": 12})

# print(dbscan.labels_)

n_clusters= len(set(dbscan.labels_))-(1 if -1 in dbscan.labels_ else 0)
# print(np.count_nonzero(smaple_cores))
print("Number of Clusters Formed:", n_clusters)
print("silhouette_score DBSCAN:", silhouette_score(X_data,dbscan.labels_))
print("silhouette_score KMEANS:", silhouette_score(X_data,kmeans.labels_))
n_noise_ = list(dbscan.labels_).count(-1)
print("Number of Noisy datapoints:", n_noise_)

# # The dbscan plot
db_colors = [fte_colors[label] for label in dbscan.labels_]
# ax2.scatter(X_data[:, 0], X_data[:, 1], c=db_colors)
ax2.set_title(f"DBSCAN\nSilhouette: {dbscan_silhouette}", fontdict={"fontsize": 12})

# ax = plt.axes(projection='3d')
# ax.scatter(X_data[:, 0], X_data[:, 1], X_data[:, 2], c=db_colors, cmap='viridis', linewidth=0.5);

# plt.show()


ari_kmeans = adjusted_rand_score(df['class'], kmeans.labels_)
ari_dbscan = adjusted_rand_score(df['class'], dbscan.labels_)

print("Adjusted Score KMEANS : ", ari_kmeans)
print("Adjusted Score DBSCAN : ", ari_dbscan)