__author__ = 'albertogonzalezpaje'

# Objective: Download, read and scrape a List of URLs
# Reference URL: http://finance.yahoo.com/q/cp?s=%5EIXIC
# Sistema de paginacion: Pagina_1 = http://finance.yahoo.com/q/cp?s=%5EIXIC
# Pagina_2 = http://finance.yahoo.com/q/cp?s=%5EIXIC&c=1

# Working directory
import os
os.getcwd()
os.chdir('/Users/albertogonzalezpaje/Desktop/python/python_data_analysis/stocks/markets')
print os.getcwd()


from pattern.web import URL, DOM, plaintext
import pprint
import csv
from time import sleep
import random
# http://finance.yahoo.com/q/cp?s=%5EIXIC&c=


URL_YAHOO = "http://finance.yahoo.com/q/cp?s=%5EBVSP&c="
URL_OUTPUT = "tickets.csv"
URL_ERROR = "tickets_error.csv"
INIT_PAGE = 0
ROWS_PATH = ".yfnc_tableout1 tr table tr"
CELLS_PATH = ".yfnc_tabledata1"
NUM_PAGES = 2
TICKETS = []


def loadPage(numPage):
    #Load the content from the given page
    url = URL(URL_YAHOO + str(numPage))
    dom = DOM(url.download(cached=True))
    for row in dom(ROWS_PATH)[1:]:
        #pprint.pprint(plaintext(row(CELLS_PATH)[0].content))
        TICKETS.append({"symbol": plaintext(row(CELLS_PATH)[0].content), "name": plaintext(row(CELLS_PATH)[1].content) })
    pprint.pprint(str(numPage + 1) + "/" + str(NUM_PAGES))


def saveCSVFromArray(inputData,urlFile):
    #Save CSV from input Array
    out = csv.writer(open(urlFile, "wb"), delimiter=';', quoting=csv.QUOTE_ALL)
    out.writerow(["symbol", "name"])
    for source in inputData:
        out.writerow([source["symbol"],source["name"]])

def main():
    for i in range(INIT_PAGE,NUM_PAGES):
        try:
            #sleep(random(1000, 2000))
            loadPage(i)
        except URL_ERROR as e:
            saveCSVFromArray(TICKETS,URL_ERROR)
    saveCSVFromArray(TICKETS,URL_OUTPUT)


if __name__ == "__main__":
    main()







