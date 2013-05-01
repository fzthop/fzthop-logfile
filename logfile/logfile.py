#!/usr/bin/python
#Filename: logfile.py

import os
import sys
import time
import shutil

class filelog:

	def lastlog(self):
		os.system("last")

	def bootlog(self):
		os.system("chkconfig --list")
		os.system("grep error /var/log/boot.log")

	def secure(self):
		shutil.copyfile("/var/log/secure", "/root/log/logfile/secure.txt")
		datenu = time.strftime('%b %d', time.localtime(time.time())) #Get current time, but, how to get another day's logs?
		key = "sshd" #just get ssh
		f = open('/root/log/logfile/secure.txt', 'r')
		try:
			for line in f:
				if datenu in line:
					if key in line:
						print line
		finally:
			f.close()

	def maillog(self):
		shutil.copyfile("/var/log/maillog", "/root/log/logfile/maillog.txt")
		datenu = time.strftime('%b %d', time.localtime(time.time()))
		f = open('/root/log/logfile/maillog.txt', 'r')
		try:
			for line in f:
				if datenu in line:
					print line
					
		finally:
			f.close()


