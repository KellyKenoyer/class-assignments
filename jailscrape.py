import urllib2, csv
#This line imports two python libraries
from bs4 import BeautifulSoup
#this imports the BeautifulSoup library
outfile = open('jaildata.csv', 'w')
#This line creats a csv to pull data into
writer = csv.writer(outfile)
#this line tells python to write to the chosen outfile (jaildata.csv)
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#This line sets the relevant URL for the scrape
html = urllib2.urlopen(url).read()
#This line opens the webpage and reads it

soup = BeautifulSoup(html, "html.parser")
#This line parses the website

tbody = soup.find('tbody', {'class': 'stripe'})
#This line tells python to find the "tbody" section of the html code of the URL and pull all the data from class to stripe.

rows = tbody.find_all('tr')
#This line tells python to find the "tr" section of the html code of the URL within tbody
for row in rows:

    cells = row.find_all('td')
    #This line creates a term called "cell" to dump data into pulled from the rows of data on the website, then has python pull that data (called "td" in HTML)

    data = []
    for cell in cells: