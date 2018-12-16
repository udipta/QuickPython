import os,datetime,time

os.setuid(os.geteuid())

hourHand = datetime.datetime.now().hour
while True:
    if hourHand == 20:
        minuteHand = datetime.datetime.now().minute
        if 0 <= minuteHand <30:
            command = "notify-send -t 0 \"Hey udipta! go have Food and come back.\" "
			p = os.system('%s' % (command))
			time.sleep(30)
        else:
			continue
