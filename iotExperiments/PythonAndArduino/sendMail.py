#!/usr/bin/python
import serial
import serial.tools.list_ports
from smtpMandrill import *
import re, time

def resetArduino(arduino):
	# Toggle DTR to reset Arduino
	arduino.setDTR(False)
	time.sleep(1)
	# toss any data already received, see
	# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
	arduino.flushInput()
	arduino.setDTR(True)

decision = raw_input("Do you want to use default settings (y/n): ")
#Mail dictionary
mail = {}

#Basic requirements for sending the message
if decision == 'n' or decision == 'N':
	mail['apiKey'] = raw_input("Enter your api key: ")
	mail['content'] = raw_input("Enter the mail['content']of your message: ")
	mail['subject'] = raw_input("Enter the subject: ")
	mail['fromEmail']= raw_input("Enter the from email address: ")
	mail['toEmail']= raw_input("Enter the to email address: ")
else:
	mail['apiKey']= '<DEFAULT_API_KEY>'
	mail['content']= 'This is mail from Arduino'
	mail['subject']= 'Arduino email sender'
	mail['fromEmail']= 'testmail@gmail.com'
	mail['toEmail']= '<default>@gmail.com>'

#Get all the port name to detect the correct port for microcontroller/Arduino
ports = list(serial.tools.list_ports.comports())
portName = False
for p in ports: #Iterating thought all the ports
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

	word = ser.readline() #Read the line from the serial monitor
	word = " ".join(re.findall("[a-zA-Z0-9]+", word)) #Extract only the alphabets form what is transimitted through the serial monitor
	#print word
	if word.lower() == '1':
		print "You pressed a button, going to send a mail"
		sendMail(mail)
		print "Mail sent successfully"
		os.system('notify-send "Mail sent successfully"');
		exit(0)