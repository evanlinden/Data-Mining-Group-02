#Group 2
#CSPB 4502 - Data Mining
#Final Project

#Workflow: AddChangedColumn -> TruncateColumns -> MergeDatasets -> OptimizeClusterCount -> ClassifyData

#Import relevant libaries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

#Import merged data csv
mergeddata = pd.read_csv("mergeddata.csv")

#Value derived from OptimizeClusterCount.py
k = 38

#Run kMeans classifier with optimal cluster count
kmeans = KMeans(n_clusters=k).fit(mergeddata.set_index('symbol').to_numpy())

#Pull list of symbols and assigned labels for each symbol
symbolslist = mergeddata["symbol"].values.tolist()
labelslist = kmeans.labels_

#Zip columns together and create results dataframe
zippedlist = np.column_stack((symbolslist,labelslist))
resultsdf = pd.DataFrame(zippedlist,columns = ['symbol','cluster'])

#Print final dataframe and save into final csv: mergeddata.csv
print(resultsdf)
resultsdf.to_csv("results/resultscombined.csv")

#Create and save a .csv for each cluster
for i in range(1,k):
    clusterdf = resultsdf[resultsdf['cluster']==str(i)]
    savestring = "results/results" + str(i) + ".csv"
    clusterdf.to_csv(savestring) 