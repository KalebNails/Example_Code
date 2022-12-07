#Kaleb Nails
#Created 12/6/2022
#Modified: 12/6/2022

#Purpose: Send dummy data to a MaMa duck for it to transmit.
from encodings import utf_8
import serial
import time
import random





ser = serial.Serial(port = '/dev/ttyUSB0',baudrate=115200,bytesize=8)
ser.flush


while True:
    T = 22 + random.random()
    H = 75 + random.random()
    roll = 0 + random.random()
    pitch = 0 + random.random()
    yaw = 25 + random.random()
    U = 0 + random.random()
    V = 0 + random.random()
    W = 0 + random.random()
    lat = 22.52 + random.random()
    lon = -81.20 + random.random()
    alt = 0  + random.random()
    pressure = 0 + random.random() 
    gpstime = 11172365 + random.random() 
    logfile_size = 765 + random.random()



    #test_float = [1.545, 'hi',-0.6, 128]
    test_float = [T, H, roll, pitch, yaw, U, V,W, lat, lon, alt, pressure, gpstime, logfile_size]
    test_string = str(test_float)
    #print(test_string)
    test_bytes = bytes(test_string, 'utf-8')
    print(test_bytes)
    ser.write(test_bytes)
    print("sent")
    time.sleep(2)

#ser.write(bytes(test_string))
