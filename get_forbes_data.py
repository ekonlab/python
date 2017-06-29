__author__ = 'albertogonzalez'


import requests
from lxml import html
import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup as BS
import urllib2


# set working directory: os.chdir(path)
os.chdir("/home/albertogonzalez/Desktop/bestiario/Quadrigram/Quadrigram_HTML5/2015/clientes/forbes")
print(os.getcwd() + "\n")


# Company Info 1

page_1 = "http://www.forbes.com/companies/icbc/"

def scrap(page):
    response = requests.get(page)
    tree = html.fromstring(response.text)
    company_logo = tree.xpath('//img[@class="main_info_img"]/@src')
    company_name = tree.xpath('//div[@class="data has_image"]/h1/text()')
    company_market_cap = tree.xpath('//li[@class="amount"]/text()')
    lista = [company_logo,company_name,company_market_cap]
    return lista

page_info_1 = scrap(page_1)
#print page_info_1


# Company Info 2
import urllib
file = urllib.urlopen(page_1)
from bs4 import BeautifulSoup
soup = BeautifulSoup(file)
li = soup.findAll('dd')
page_info_2 = [str(i) for i in li]
page_info_3 = page_info_2[0:8]

#print page_info_3

page_info_total = page_info_1 + page_info_3
#print page_info_total


'''
GENERATE COMPANY INFO FOR N COMPANIES
'''

# Load and Read the file with the companies' URLS
alist = [line.rstrip() for line in open('companies_urls.csv')]
print alist[1:10]


## Use the function
# Testing
tes = alist[1:5]
print tes

# To all
foo = [scrap(i) for i in tes]
print foo


np.savetxt("companies_data_2.txt", foo, delimiter=",", fmt='%s')







###################### INVALID CODE ########################################
'''
theoric xpath path for industry: //*[@id="left_rail"]/div[1]/div[1]/dl[1]/dt
# Second approach - beautiful soup -

html_doc = "http://www.forbes.com/companies/icbc/"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
soup.title
s = soup.find("dt",text="Industry").next_sibling.contents[0]



# Third approach with Beautiful Soup

url ="http://www.forbes.com/companies/icbc/"
usock = urllib2.urlopen(url)
data = usock.read()
usock.close()
soup = BS(data)
print soup.find('dt', {'name':'Industry'}).text


# Fourth approach
import urllib
f = urllib.urlopen("http://www.forbes.com/companies/icbc/")
s = f.read()
f.close()

from bs4 import BeautifulStoneSoup
soup = BeautifulStoneSoup(s)
inputTag = soup.find(attrs={"name" : "Industry"})
output = inputTag['value']
print output
'''






