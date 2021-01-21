from datetime import datetime
import os

def check_time_min():
	""" Returns minute for users"""
	timestamp = datetime.now()
	hour = timestamp.hour
	minute = timestamp.minute
	second = timestamp.second
	hm = (hour,minute,second)
	return hm

def sey_hello(username):
	return "Hello {}".format(username)

def shutdown():
	os.system("shutdown -p")
