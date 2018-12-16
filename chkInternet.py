#!/usr/bin/python3
def chkNet():
	import requests
	try:
		response = requests.get("https://www.google.com" verify=False, timeout=5)
		#return True
		print('\tCongrats! YOU ARE ONLINE NOW \n')
	except requests.ConnectionError:
		#return False
		print('\tSorry! YOU ARE OFFLINE NOW \n')

chkNet()

