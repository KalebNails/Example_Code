#from cobs import cobs
#THIS IS THE RECIEVING EXAMPLE, works correctly

#To run in terminal its: python Serialtestsend.py
from socket import timeout
from sqlite3 import DatabaseError
import serial #This is from pyserial
import time
import struct
import ctypes
import code # drop into a python interpreter to debug: code.interact(local=dict(globals(), **locals()))
#new attempt with Cobs library
from cobs import cobs

flag ='|'
flag = flag.encode()

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
        #timeout = 10
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
        #datadecode = data.decode()
        #print(datadecode)
  
        #struct.upack('fff',data)

        
        
