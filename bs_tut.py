from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uo

#scrape from website link
my_url = 'https://uk.tradingview.com/markets/cryptocurrencies/prices-all/'
client = uo(my_url)
page_html = client.read()
client.close()

#html parser
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)