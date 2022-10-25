#Kaleb Nails
#Created: 10/3/2022
#Modified: 10/25/2022
# Originally: input_test.py
#Purpose: This decodes 4 floats that where packaged using COBS library that come in from a hellteck. 
#This hellteck is using Packetresponse which was renamed to Sending_Float.ino 
#in the C section of my github. 

#THIS IS THE RECIEVING EXAMPLE, works correctly

import serial #This is from pyserial
import time
import struct

# new attempt with Cobs library or constant overbyte stuffing. In laymens term
# binary is full of "random" charecters, so if you where to use /n as a fence 
# it might randomly cut data in half. COBS looks through it and changes the /n to some other variable,
# and then if that new flag exists somewhere else it iterates through to find a flag that will work. 
# This is my understanding of COBS.

from cobs import cobs
#import code # drop into a python interpreter to debug: code.interact(local=dict(globals(), **locals()))
#new attempt with Cobs library

#This checks if the port is open, and describes the issue if it isnt.
try:
    ser = serial.Serial(port = '/dev/ttyUSB0',baudrate=115200,bytesize=8)
    ser.flush
    ser.flushInput()

except serial.SerialException as var:
    print('an exception occurred',var)

else: 
    print('serial port opened')

    time.sleep(.2)
    #print('sending')
    time.sleep(.4)

    while True:
        data = ser.read_until(b'\x00') #use readline to send whole message, use buffer, and number of bits
        #use readuntil() to help find the code.
        #code.interact(local=dict(globals(), **locals()))
        n = len(data)
        #print(data)
        data = data[0:n-1]
        print('data=',data)
        try:
            dataDecoded = cobs.decode(data)
            #dataDecoded = struct.unpack(data)
            readable = struct.unpack('ffff', dataDecoded)
            print(readable)
            #data = data [1:]
            #print(dataDecoded)
        except cobs.DecodeError as err:
            print(f"Unexpected {err=}, {type(err)=}")
