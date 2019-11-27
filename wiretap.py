#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import random
import hashlib
import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
from datetime import datetime

class Colors:
	Header = "\033[93m"
	Ok     = "\033[92m"
	Fail   = "\033[91m"
	Normal = "\033[0m"

def Record():
	#User Defined Record Time
	seconds = 30
	# MD5 String from Randomly Generated Number for Filename
	hash = hashlib.md5(b'RND:' + str(random.randint(1, 1000000) * 5))
	hash = hash.hexdigest().upper()
	# Filename to Save As
	now = datetime.now()
	dt = now.strftime("%H%M%S-%Y")
	filename = hash + "--" + dt + ".wav"
	print ('{:*^69}'.format(" " + Colors.Header + "WireTAP" + Colors.Normal + " "))
	try:
		print ("[" + Colors.Ok + "+" + Colors.Normal + "] Recording for " + Colors.Ok + str(seconds) + Colors.Normal + " Seconds from Microphone")
		record = sd.rec(int(seconds * 44100), samplerate=44100, channels=2)
		sd.wait()
		print ("[" + Colors.Ok + "+" + Colors.Normal + "] Saving " + Colors.Ok + filename + Colors.Normal)
		write(filename, 44100, record)
	except IOError:
		print ("[" + Colors.Fail + "X" + Colors.Normal + "] Error Saving File, Check Permissions")
	except Exception:
		print ("[" + Colors.Fail + "X" + Colors.Normal + "] An Unknown Error Has Occured")

def Help():
	print ("Usage:")
	print ("	python wiretap.py --record			- " + Colors.Header + "Starts recording" + Colors.Normal)
	print ("	python wiretap.py --delete [filename]		- " + Colors.Header + "Deletes .wav Recording" + Colors.Normal)
	print ("	python wiretap.py --upload-ftp [filename]	- " + Colors.Header + "Uploads file to FTP Server (Not Implemented Yet)" + Colors.Normal)
	print ("	python wiretap.py --help			- " + Colors.Header + "Displays this message" + Colors.Normal)

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		if (sys.argv[1] == "--record"):
			Record()
		elif (sys.argv[1] == "--delete"):
			if (sys.argv[2].endswith('.wav')):
				os.remove(sys.argv[2])
				print ("Deleting:" + sys.argv[2])
			else:
				print ("Not a vaild .wav file")
		elif (sys.argv[1] == "--upload-ftp"):
			print ("This function will be added in a later release")
		elif (sys.argv[1] == "--help"):
			Help()
		else:
			Help()
	else:
		Help()