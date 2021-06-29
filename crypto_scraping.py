from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uo
import csv

#scrape from website link
my_url = 'https://uk.finance.yahoo.com/cryptocurrencies?count=100&offset=0'
client = uo(my_url)
page_html = client.read()
client.close()


#html parser
page_soup = soup(page_html, "html.parser")
#print(page_soup.h1)

#calling specific items
columns = page_soup.findAll("th")
items = page_soup.findAll("tr", {"class": "simpTblRow"})
#i = items[0]
#print(i.td.a.text)

#writing scraped data to csv file
filename = "crypto_scraped_data.csv"
f = open(filename,"w")

#converting header values from list to csv format
titles = []
for c in columns[:10]:
    titles.append(c.span.text)
wr = csv.writer(f, quoting=csv.QUOTE_ALL)
wr.writerow(titles)
#headers = ",".join(titles)

#converting item values from list to csv format
#rows = []
row_item = []
for item in items:
    i = item.findAll("td")
    for x in i[:10]:
        #print(x.text)
        row_item.append(x.text)
    #rows.append(row_item)
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(row_item)
    row_item = []
    #print("-------------")
f.close()
