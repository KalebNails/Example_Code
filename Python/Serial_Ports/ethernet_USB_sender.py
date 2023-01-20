#Author: Kaleb Nails
#Created: 1/10/2023
#modified: 1/20/2023
#Purpose: This is running on a rasberry PI that has its eithernet plug into another computer. 
# a great instruction video about this process is: https://www.youtube.com/watch?v=S7Yle8clJ30

import socket
#msgtosend = '[value:103,value2: 1.34]'
time_example = 1.4
msgtosend = '{"Sensor": "PurpleAir0", "value":"%s"}' %(time_example)

#This is hardcoded per computer
ServerAddress = ('169.254.26.44',2222)
bufferSize = 1024

bytestosend = msgtosend.encode('utf-8')

#This creates the default socket settings and sends the buffer
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClient.sendto(bytestosend,ServerAddress)

