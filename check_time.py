from datetime import datetime

def check_time_min():
	""" Returns minute for users"""
	timestamp = datetime.now()
	hour = timestamp.hour
	minute = timestamp.minute
	hm = (hour,minute)
	return hm

