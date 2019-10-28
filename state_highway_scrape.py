import requests
from bs4 import BeautifulSoup

url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction"

dictionary = {'searchDate' : '10/31/2017'}

r = requests.post(url, data=dictionary)

print(r.text)