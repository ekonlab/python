__author__ = 'albertogonzalezpaje'
# Reference URLs
# http://results.chicagomarathon.com/2013/?page=1&event=MAR&lang=EN_CAP&num_results=1000&pid=search&search_sort=name
# http://results.chicagomarathon.com/2013/?page=39&event=MAR&lang=EN_CAP&num_results=1000&pid=search&search_sort=name

# Import

from pattern.web import URL, DOM, plaintext
import pprint
import csv

# Variables

url_estruc_1 = "http://results.chicagomarathon.com/2013/?page="
url_estruc_2 = "&event=MAR&lang=EN_CAP&num_results=1000&pid=search&search_sort=name"
init_page = 1
last_page = 3
output_file = "chicago_marathon.csv"
output_file_error = "chicago_marathon_error.csv"
ROWS_PATH = ".list-table"
CELLS_PATH = ". list-highlight td"
RESULTS = []

# Load + Extract

def loadPage(numPage):
    #Load the content from the given page
    url = URL(url_estruc_1 + str(numPage) + url_estruc_2)
    dom = DOM(url.download(cached=True))
    for row in dom(ROWS_PATH)[1:]:
        #pprint.pprint(plaintext(row(CELLS_PATH)[0].content))
        RESULTS.append({"place": plaintext(row(CELLS_PATH)[0].content), "place_gender": plaintext(row(CELLS_PATH)[1].content) })
    pprint.pprint(str(numPage + 1) + "/" + str(last_page))

# Save Array as CSV

def saveCSVFromArray(inputData,urlFile):
    #Save CSV from input Array
    out = csv.writer(open(urlFile, "wb"), delimiter=',', quoting=csv.QUOTE_ALL)
    out.writerow(["place", "place_gender"])
    for source in inputData:
        out.writerow([source["place"],source["place_gender"]])

def main():
    for i in range(init_page,last_page):
        try:
            loadPage(i)
        except output_file_error as e:
            saveCSVFromArray(RESULTS,output_file_error)
    saveCSVFromArray(RESULTS,output_file)


if __name__ == "__main__":
    main()

