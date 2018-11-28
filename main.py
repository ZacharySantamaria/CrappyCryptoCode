import requests
from bs4 import BeautifulSoup as bs4
import time

def bitcoin(content):
	#prints very specifc portion of the array to find the price
	print('the value of ' + content[1][1:4]+ ' is '+ content[1][26:34])

def Monero(content):
	#print very specific portion of the content array
	print('The value of ' + content[11][2:5] + ' is ' + content[11][25:31])

def loadPageCM():
	#Grabbing url with requests
	page = requests.get('https://www.coinmarketcap.com')
        
    #Sending page to Bs4 to parse info
	soup = bs4(page.text, 'html.parser')
        
	divs = soup.findAll('table', id='currencies')
        
	content = []
        
    #finds all div tags and loops through them
	for div in divs:
		rows = div.findAll('tr')
		for row in rows:
     		#looping through all the row in the singular div
			#appending to content array and removing the ending portion
			content.append(row.text.replace('\n', '')[:-115])
	
	return content

while True:
	
	content = loadPageCM()
	bitcoin(content)
	Monero(content)
	time.sleep(60)	
	
