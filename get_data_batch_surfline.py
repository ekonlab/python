
'''

1.- SURFLINE

endpoint: http://api.surfline.com/v1/forecasts/<spot_id>?resources=&days=&getAllSpots=&units=&usenearshore=&interpolate=&showOptimal=&callback=

3843
2137
2138
2139

'''


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib, json
import pandas as pd


def get_info_name(name):
    n1 = "http://api.surfline.com/v1/forecasts/"
    n2 = name
    n3 = "?resources="
    n4 = "surf"
    n5 = "&days=5&getAllSpots=true"

    nf = n1 + n2 + n3 + n4 + n5

    print nf

    url = nf
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data[0]

    frame = pd.DataFrame(data)
    return frame



lines = [line.rstrip('\n') for line in open('spots.txt')]
print lines

data = map(get_info_name, lines)
print data


#dframe = pd.DataFrame(data,columns=headers)



# EXECUTE FROM CONSOLE: python get_names.py >> text.log

# CREATE AND MANAGE DATABASE - SQLITE 3

'''
create db: terminal: sqlite3 name.db
list tables: .tables
exit: .exit

'''

# import sqlite3
# print sqlite3.version
# import os
# os.chdir("/Users/albertogonzalez/Desktop/best/surf")
# print os.getcwd()
#
# # connect to sqlite3
# import sys
#
# conn = sqlite3.connect("surfline.db")
# print conn
#
#
# dframe.to_sql(name='surf_table', con=conn, if_exists = 'append', index=True)
#








































