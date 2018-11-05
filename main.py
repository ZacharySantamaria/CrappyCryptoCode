import requests
from bs4 import BeautifulSoup as bs4
import time

while True:
	#Grabbing url with requests
	page = requests.get('https://www.coinmarketcap.com')
	
	#Sending page to Bs4 to parse info
	soup = bs4(page.text, 'html.parser')
	
	divs = soup.findAll('table', id='currencies')
	
	content = []
	
	for div in divs:
		rows = div.findAll('tr')
		for row in rows:
			content.append(row.text.replace('\n', '')[:-115])
			#print(type(row))
	
	print('the value of ' + content[1][1:4]+ ' is '+ content[1][27:35])
	time.sleep(60)	
	


'''Attempts'''
#table = soup.find('table' , id='currencies')
#
#row = table.find('tr')
#
#
#index = 1
#
#for rows in range(1,101):
#	number = row.findAll('td').text.strip() 	
#	print(number)
#	index = index + 1	
#	
#
#	#if index <= 9:
#	#	name = row[index].text.strip().replace('\n', '')[1:4]
#	#	print(name)
#	#	price = row[index].text.strip().replace('\n', '')[0:-123]
#	#	print(price)
#	#	index = index + 1	
#
#	#elif index > 9 and index <= 99:
#	#	name = row[index].text.strip().replace('\n', '')[2:5]
#	#	print(name)
#	#	price = row[index].text.strip().replace('\n', '')[0:-123] 	
#	#	print(price)
#	#	index = index + 1
#
#	#elif index > 99:
#	#	name = row[index].text.strip().replace('\n', '')[3:6]     			
#	#	print(name)	
#	#	price = row[index].text.strip().replace('\n', '')[0:-123] 
#	#	print(price)
#	#	index = index + 1
#
#
##naming works... Next is the price. find a way to search between $$
#print(row[100].text.strip().replace('\n', '')[3:6])


#for rows in row:
#   print(row.text) 



