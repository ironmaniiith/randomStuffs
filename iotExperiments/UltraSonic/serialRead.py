#!/usr/bin/python
import serial
import serial.tools.list_ports
import re, time
import os

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
	# print p
	if p[2] == 'USB VID:PID=2341:0043 SNR=554343436333515122A1': #Given arduino board info
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

while True:
	word = arduino.readline() #Read the line from the serial monitor
	try:
		distance = str(word)
		print distance
		# We can also add some condition on the distance here
		# Add stabilizer function for getting the stable distance here
	except:
		print "Some error occured"