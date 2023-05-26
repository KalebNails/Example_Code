#Author: Kaleb Nails
#Created: 5/23/2023
#Modified: 20/26/2023
#Purpose: To send prerecorded data to the bokeh dashboard for it to be interpereted. 


#Below is the genereal format for data as its printed of the sensors code

#dateStr =', Date:, {0}'.format(datetime.now())
#    dataStr2 = ', Data2:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata2["particles 03um"],aqdata2["particles 05um"],aqdata2["particles 10um"],aqdata2["particles 25um"],aqdata2["particles 50um"],aqdata2["particles 100um"])
#    dataStr1 = ', Data1:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata["particles 03um"],aqdata["particles 05um"],aqdata["particles 10um"],aqdata["particles 25um"],aqdata["particles 50um"],aqdata["particles 100um"])
#     file.write(dateStr + dataStr1 + dataStr2 + "\n")


import pandas as pd
import time
import socket
import json

#This is the internal IP cod
ServerAddress = ('10.33.142.235',2222)#'169.254.26.44',2222)
bufferSize = 1024

# Read the CSV file#data = pd.read_csv('2023_01_25__16_40_10_ttyACM0_alphasense_opc_n3.csv')
data = pd.read_csv('2023_03_30__18_41_13_ttyACM1_alphasense_opc_n3.csv')

# Iterate over each row in the DataFrame
message = {}
for index, row in data.iterrows():
    # Access data from each column and label it
    #message = {"Sensor":"Purpleair0","date":row[0],"cnt":row[1], 'T_samp': row[2], "SFR": row[3], "temp": row[4], "RH": row[5], "PMA":row[6],"PMB":row[7],"PMC":row[8]}
    message = {"Sensors":"Alphasense0", 'T_samp': row[4], "SFR": row[6], "temp": row[8], "RH": row[10], "PMA":row[12],"PMB":row[14],"PMC":row[16]}
    print((message))

    #turns cell into a string then bytes
    message_string = json.dumps(message)
    bytestosend = message_string.encode('utf-8')

    try:
        #This creates the default socket settings and sends the buffer
        UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        UDPClient.sendto(bytestosend,ServerAddress)

    except:
        print('eithernet failed')
        pass

    # Add a 2-second buffer to simulate real life lag
    time.sleep(2)
