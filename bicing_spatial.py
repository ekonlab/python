__author__ = 'albertogonzalez'

# Import modules
import pandas as pd
import numpy as np
from pandas import DataFrame
# import pysal
from scipy.cluster.vq import kmeans2, whiten
import os

# Load data
bicing_location_df = pd.read_excel("/home/albertogonzalez/Desktop/python_materials/data_analysis/spatial_data_analysis/BICING_STATIONS.xlsx",sheetname="Hoja1")
print bicing_location_df.head(10)

bicing_activity_df =  pd.read_excel("/home/albertogonzalez/Desktop/python_materials/data_analysis/spatial_data_analysis/BICING-ACTIVITY-21-4-15.xlsx",sheetname="Sheet1")
print bicing_activity_df.head(10)

# Calculate mean usage by station
bicing_activity_df_2 = bicing_activity_df.drop('ID', 1)
bicing_activity_df_2["activity_mean"] = bicing_activity_df_2.mean(axis=1)
act_mean = pd.DataFrame(bicing_activity_df_2["activity_mean"])
id_col = pd.DataFrame(bicing_activity_df["ID"])

# Get id + activity mean
bicing_activity_neat = pd.concat([id_col,act_mean],axis =1)
print bicing_activity_neat[:5]

# Merge location & activity
bicing_tot = pd.merge(bicing_location_df,bicing_activity_neat)
print bicing_tot[:5]

# Delete non needed columns
bicing_def = bicing_tot[["LATITUDE","LONGITUDE","activity_mean"]]
print bicing_def[:5]
bi = np.array(bicing_def)


# Cluster
# x = lon/lat points and y = number of cluster
x, y = kmeans2(whiten(bi), 4, iter = 20)
print x
print y

# Export cluster array
# Add ID column
df_1 = pd.DataFrame(bicing_tot["ID"])
df_2 = pd.DataFrame(y, columns=['cluster_number'])
df_3 = pd.concat([df_1,df_2],axis =1)

os.chdir("/home/albertogonzalez/Desktop/python_materials/data_analysis/spatial_data_analysis")
print(os.getcwd() + "\n")
df_3.to_csv("bicing_cluster_binning.csv")

# Generate a df with ID, mean and cluster
df_4 = pd.DataFrame(bicing_activity_neat)
df_5 = pd.concat([df_4,df_2],axis =1)
df_5.to_csv("bicing_cluster_binning_activity.csv")


################################################################################################################
'''
http://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/
'''
# Using DBSCAN to cluster
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle

coordinates = bicing_location_df.as_matrix(columns=['LONGITUDE', 'LATITUDE'])

db = DBSCAN(eps=.005, min_samples=1).fit(coordinates)
labels = db.labels_
print labels
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
clusters = pd.Series([coordinates[labels == i] for i in xrange(num_clusters)])
print('Number of clusters detected by DBSCAN =  %d' % num_clusters)

df_6 = pd.DataFrame(labels)
df_7 = pd.concat([df_1,df_6],axis=1)
print df_7.head()

df_7.to_csv("bicing_cluster_dbscan_activity.csv")

################################################################################################################

'''
Euclidean Distance
'''
from scipy.spatial import distance
from scipy.spatial.distance import cdist

x_data = np.array(bicing_def["LATITUDE"])
y_data = np.array(bicing_def["LONGITUDE"])

dx = x_data[..., np.newaxis] - x_data[np.newaxis, ...]
dy = y_data[..., np.newaxis] - y_data[np.newaxis, ...]
print dx

# stack in one array, to speed up calculations
d = np.array([dx,dy])
print d.shape





################################################################################################################

























