
from bs4 import BeautifulSoup
import requests, mechanize
import csv

csvfile = open('highway.csv', 'a')
hwy_writer =csv.writer(csvfile)

url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction"

dictionary = {'searchDate' : '10/31/2017'}

r = requests.post(url, data=dictionary)

print(r.text)

html = r.text

soup = BeautifulSoup(html, "html.parser")

print(soup)









