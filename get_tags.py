__author__ = 'albertogonzalezpaje'

# libraries
import requests
from lxml import html
import pandas as pd
import numpy as np

# for each post, get tags

# scrape function

def scrap(post):
    response = requests.get(post)
    tree = html.fromstring(response.text)
    entry_date = tree.xpath('//div[@class="post-single post-single-sdb"]/div[@class="entry-date"]/text()')
    print entry_date
    comments = tree.xpath('//div[@class="entry-counters clearfix"]/div[@class="entry-comments"]/a/text()')
    print comments
    title = tree.xpath('//h2[@class="entry-title"]/a/text()')
    tags = tree.xpath('//div[@class="post-single post-single-sdb"]/div[@class="entry-tags"]/a/text()')
    lista = [entry_date,comments,title,tags]
    #lista_2 = np.transpose(lista)
    #tabla = pd.DataFrame(lista_2)
    return lista


alist = [line.rstrip() for line in open('url_post_all.csv')]
print alist[1:10]


## Use the function
# Testing
tes = alist[1:50]
print tes

# To all
foo = [scrap(i) for i in alist]
print foo [1:20]
#np.savetxt("post_attributes_all.txt", foo, delimiter=",", fmt='%s')



# a = scrap("http://www.enriquedans.com/2015/05/los-facebook-instant-articles-son-un-ejemplo-de-como-competir-en-la-web-de-hoy.html")
# np.savetxt("post_attributes.txt", a, delimiter=",", fmt='%s')
# print a

#li = [i.split() for i in open("url_post_all.txt").readlines()]
#print li








