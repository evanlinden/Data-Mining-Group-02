#Group 2
#CSPB 4502 - Data Mining
#Final Project

#Workflow: AddChangedColumn -> TruncateColumns -> MergeDatasets -> OptimizeClusterCount -> ClassifyData
#Reference code: https://predictivehacks.com/k-means-elbow-method-code-for-python/

#Import relevant libaries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Import merged data csv
mergeddata = pd.read_csv("mergeddata.csv").set_index('symbol').to_numpy()

#Create distortions list
distortions = []

#Create range of possible k values
K = range(1,50,1)

#Run kMeans classfier for each possible K
for k in K:
    kmeans = KMeans(n_clusters=k).fit(mergeddata)
    distortions.append(kmeans.inertia_)

#Plot k (number of clusters) vs. distortion such that an "elbow" (the point where the derivative decreases in magnitude) can be identified.
#This inflection point reflects a good number of clusters such that the model is not too overfit, but also useful, unique clusters can be indentified.
plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()