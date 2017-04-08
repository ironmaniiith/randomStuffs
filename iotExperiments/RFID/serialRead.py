#!/usr/bin/python
import serial
import serial.tools.list_ports
import re, time
import os

myCards = {
	'1100009BA52F' : 0
	# 494948484848576665535070 is the number when Serial.print is used instead of Serial.write in main.ino
}

def resetArduino(arduino):
	# Toggle DTR to reset Arduino
	arduino.setDTR(False)
	time.sleep(1)
	# toss any data already received, see
	# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
	arduino.flushInput()
	arduino.setDTR(True)

#Get all the port name to detect the correct port for microcontroller/Arduino
ports = list(serial.tools.list_ports.comports())
portName = False
for p in ports: #Iterating thought all the ports
	# Complete info for the given arduino board is 'USB VID:PID=2341:0043 SNR=554343436333515122A1'
	if 'USB VID:PID=' in p[2]: #General arduino board info
		portName = p[0]

if portName==False:
	#This executes if board is not found
	print "Sorry Arduino board not found, do you want to enter the port name manually"
	decision = raw_input("(Y/N): ")
	if decision == 'N' or decision == 'n':
		print "Exiting"
		exit(0)
	portName = raw_input("Enter the port name (ex. /dev/ttyACM0)")

#Connect to serial monitor for the incoming data from microcontroller
arduino = serial.Serial(portName, 9600)
resetArduino(arduino)
print "Ready..."

while True:
	word = arduino.readline() #Read the line from the serial monitor
	try:
		word = str(word).strip()
		state = myCards[word]
		if state == False:
			print "Welcome",word
			myCards[word] = True
		else:
			print "Good bye", word
			myCards[word] = False
	except:
		if word:
			print "Unknown card", str(word).strip()
		else:
			print "Some error occured"