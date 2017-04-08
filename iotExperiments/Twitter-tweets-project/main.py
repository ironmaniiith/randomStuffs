#!/usr/bin/python
import serial
import serial.tools.list_ports
import re, time

LAST_LINE = -1
FILE_NAME = 'data.txt'
DELAY_BETWEEN_CONSECUTIVE_READS = 2 # In seconds

def resetArduino(arduino):
    # Toggle DTR to reset Arduino
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)

def update():
    """Reads the last line of the file determined by FILE_NAME and updates the value of LAST_LINE"""
    global LAST_LINE, FILE_NAME
    lines = None
    try:
        with open(FILE_NAME) as f:
            lines = f.readlines()
        f.close()
    except:
        pass

    if lines != None:
        is_new_value = (len(lines) > LAST_LINE)
        if is_new_value:
            LAST_LINE = len(lines)
            return True, lines[-1].strip()
    return False, None

#Get all the port name to detect the correct port for microcontroller/Arduino
ports = list(serial.tools.list_ports.comports())
portName = False

for p in ports: #Iterating thought all the ports
    if str(p[2]).count('USB VID') > 0: # == 'USB VID:PID=2341:0043 SER=554343436333515122A1': #Given arduino board info
        portName = p[0]

if portName == False:
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
    time.sleep(DELAY_BETWEEN_CONSECUTIVE_READS)
    status, value = update()
    if status:
        arduino.write(str(value)) #Read the line from the serial monitor
        print "Successfully wrote: {0}".format(value)
