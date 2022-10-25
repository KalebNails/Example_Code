# Kaleb Nails
# Created: 10/10/2022
# Modified: 10/25/2022
#Original name: RawSerialreciever.py
#
# Purpose: To read serial data from a serial port that is formated as a JSON as a JSON

import serial #This is from pyserial
import json

#This checks if the port is open, and describes the issue if it isnt.
try:
    ser = serial.Serial(port = '/dev/ttyUSB0',baudrate=115200,bytesize=8)
    ser.flush
    ser.flushInput()

except serial.SerialException as var:
    print('an exception occurred',var)
    

else: 
    print('serial port opened')

while True:
    data = ser.read_until(b'\n')
    #print(data)

    #The code block below this tries to turn a json that was turned into bytes into an object python can work with. not needed for raw serial.
    try:

        #This basically turns serial into the python object
        my_json = json.loads(data)

        #you call on the part of the object you need. sometimes [0] is needed after my_json depending on the application.
        print(my_json["Payload"])

    except json.JSONDecodeError as err:
        pass
        #print(f"Unexpected {err=}, {type(err)=}")
    





