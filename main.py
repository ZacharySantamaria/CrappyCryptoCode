import requests
from bs4 import BeautifulSoup as bs4
import time

#We should add other crypto coins in functions
#formatt in a better way.


while True:
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
			content.append(row.text.replace('\n', '')[:-115])
	
	#prints very specifc portion of the array to find the price
	print('the value of ' + content[1][1:4]+ ' is '+ content[1][27:35])
	time.sleep(60)	
	
