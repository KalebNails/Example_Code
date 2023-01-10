#Author: Kaleb Nails
#Date: 1/10/2023
#Purpose: an simple example to recieve data over a eithernet to USB port 
# from a rasberry pi sending data to the assigned serial port


import socket
import time
# cd .\OneDrive\Desktop\first_python\
bufferSize = 1024

#This is the IP of the laptop
ServerPort = 2222
ServerIP = '169.254.26.44'

#This creates the default socket settings, generally these should be fine,
#Then it bind those setting to a IP and port
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP,ServerPort))

#This prevents the recvfrom call from blocking the rest of the program from running
RPIsocket.setblocking(False)
socket
while True:
    try:
        message, address = RPIsocket.recvfrom(bufferSize)
        readable = message.decode('utf-8')
        print(readable)
    
    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError:
        pass

    finally:    
        #print('hi')
        pass