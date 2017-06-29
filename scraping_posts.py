__author__ = 'albertogonzalezpaje'


import requests
from lxml import html
import pandas as pd
import numpy as np

# Function to get the posts titles + URLs

def titulos(pagina):
    response = requests.get(pagina)
    tree = html.fromstring(response.text)
    titul = tree.xpath('//h2[@class="entry-title"]/a/@title')
    enlace = tree.xpath('//h2[@class="entry-title"]/a/@href')
    tabla = pd.DataFrame(titul,enlace)
    return tabla

# Array of posts pages
l = list(range(2,746,1))
first = "http://www.enriquedans.com/page/"

this = [first + str(i) for i in l]

# Execute the scraping function to the array of urls

all_post = [titulos(t) for t in this]
np.savetxt("all_post.csv", all_post, delimiter=",", fmt='%s')
print all_post [1:25]



