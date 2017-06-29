__author__ = 'albertogonzalezpaje'
'''
Get a list of topics covered in www.enriquedans.com
'''
import requests
from lxml import html
import pandas as pd
from math import ceil


# 1.- Read list of topics in www.enriquedans.com/temas

# Get data
response = requests.get("http://www.enriquedans.com/temas")
tree = html.fromstring(response.text)

# Extract list of topics and number of posts per topic
topics = tree.xpath('//div[@class="this-theme-etiquetas"]/a/text()')
posts = tree.xpath('//div[@class="this-theme-etiquetas"]/a/@title')
list_li = tree.xpath('//div[@class="this-theme-etiquetas"]/a/@href')

print len(topics)
print len(posts)
print len(list_li)


# Convert extracted data
df = pd.DataFrame(topics,posts)
print df
#df.to_csv('topics.csv',encoding='utf-8')







