

from socket import timeout
from sqlite3 import DatabaseError
import serial #This is from pyserial
import time
import struct
import ctypes
import json
import code # drop into a python interpreter to debug: code.interact(local=dict(globals(), **locals()))
#new attempt with Cobs library
from cobs import cobs



#This checks if the port is open, and describes the issue if it isnt.
while True:
    try:
        ser = serial.Serial(port = '/dev/ttyUSB0',baudrate=115200,bytesize=8)
        ser.flush
        ser.flushInput()

        

    except serial.SerialException as var:
        print('an exception occurred',var)
        time.sleep(2)

    else: 
        print('serial port opened')
        break

while True:
    data = ser.read_until(b'\n')
    #print(data)
    #print('_'*10)

    #The code block below this tries to turn a json that was turned into bytes into an object python can work with
    try:

        #This basically turns serial into the python object
        data = data.decode('raw_unicode_escape').replace("'", '"')
        #print(data)
        my_json = json.loads(data)
        print(my_json)
        #my_json = json.loads(data.decode("utf-8","ignore"))
        #my_json = json.loads(struct.unpack('f',data))

        #you call on the part of the object you need. sometimes [0] is needed after my_json depending on the application.
        byte_Data = (my_json["Payload"].encode('raw_unicode_escape'))
        print(byte_Data)

        readable = struct.unpack('ff',byte_Data)
        print(readable)
        #print(my_json["Payload"])
        #dataDecoded = my_json["Payload"]
        #readable = struct.unpack('f', dataDecoded)
        #print(readable)
        
    except json.JSONDecodeError as err:
        pass
        #print(f"Unexpected {err=}, {type(err)=}")