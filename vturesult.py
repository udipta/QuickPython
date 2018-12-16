from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time , csv


def connectdriver(value, link):	
	options = Options()
	options.add_argument("--headless")
	driver = webdriver.Firefox(firefox_options=options, executable_path="/usr/bin/geckodriver")
	driver.get(link)
	user = driver.find_element_by_xpath('//input[@name = "lns"]')
	user.send_keys(value)
	driver.find_element_by_xpath('//input[@id = "submit"]').click()
	webpage = driver.page_source
	driver.quit()
	return webpage

def copyList(n, table):
#	global table
	dst = []
	while n<len(table):
		dst.append(table[n])
		n=n+6
	return dst


def scrapdata(page):
	soup = BeautifulSoup(page, 'lxml')
	
	usn = soup.find('td', style="padding-left:15px;text-transform:uppercase")

	name = soup.find('td', style='padding-left:15px')

	data = soup.find_all('div', class_='divTableCell')


	table = [data[i].string.extract() for i in range(6,len(data)-5)]
	sem = table[:54]
	header = copyList(0,sem)
	header.insert(0,'NAME')
	header.insert(0,'USN')

	USN = [x.string.extract() for x in usn][-1]
	candidate = [y.string.extract() for y in name][-1]

	details = copyList(5,table)
	details.insert(0,candidate)
	details.insert(0,USN)
		
	return header, details


def USNlist():
	usn = input('Enter the starting USN: ')
	start = int(usn[-3:])
	end = int(input('Enter the last USN: ')[-3:]) +1
	USNpattern = usn[:-3]
	usnlist = []
	for i in range(start,end):
		usnlist.append(USNpattern+str(i))

	return usnlist


def makeCSV(details):
	myFile = open('result.csv', 'a')  
	with myFile:  
   		writer = csv.writer(myFile)
   		writer.writerows(details)


def generateresult():
#	mode = input('REGULAR/REVAL').upper()
	USNseries = USNlist()

#	if mode == 'REGULAR':
#		link = 'http://results.vtu.ac.in/vitaviresultcbcs/index.php'
#	elif mode == 'REVAL':
#		link = 'http://results.vtu.ac.in/vitavirevalresultcbcs/index.php'
	
	result =[]
	for value in USNseries:
		try:
			webpage = connectdriver(value, 'http://results.vtu.ac.in/vitaviresultcbcs/index.php')
			if value == USNseries[0]:
				result.append(scrapdata(webpage)[0])
			result.append(scrapdata(webpage)[1])
		except Exception as e:
			continue
		
	makeCSV(result)

generateresult()



