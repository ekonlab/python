__author__ = 'albertogonzalez'


'''
############ API TIPI CIUDADANO ####################
URL: "http://tipiciudadano.es/api/v1/tipis?offset=1&limit=1000"
'''

# LOAD PACKAGES
import json
import os
from pandas import DataFrame
from pandas import Series
import pandas as pd
import numpy as np
import urllib2

os.chdir("/home/albertogonzalez/Desktop/visualizar16")
print(os.getcwd() + "\n")

# READ API ENDPOINT JSON DATA
response = urllib2.urlopen("http://tipiciudadano.es/api/v1/tipis?offset=1&limit=1000")
data = json.load(response)
print data

# CONVERT OUTPUT LIST INTO DATAFRAME
data_df = pd.DataFrame(data)
print data_df.head()
print data_df.shape


# SPLIT TIPIS
tipis_df = data_df[['_id','dicts']]
print tipis_df.head()
print tipis_df.shape

t = tipis_df[['dicts']]
print t.head()
print type(t)


t_list = list(t)
print type(t_list)

t_list_split = [x.strip() for x in t_list.split(',')]


# SPLIT TESTS
# 1.- Create a list
a = t['dicts']
# 2.- Transform the list into a string
b = str(a)
myList = [i.split('\,')[0] for i in a]




