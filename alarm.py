import os,datetime

os.setuid(os.geteuid())

hourHand = datetime.datetime.now().hour
while True:
	
	if hourHand == 8:
		
		minuteHand = datetime.datetime.now().minute
		
		if minuteHand == 30:
			os.chdir('myCommand')
			os.system('mpg123 -q Balasese.mp3')
			break

		else:
			continue