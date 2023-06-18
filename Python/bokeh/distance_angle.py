import serial
import socket
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

#This checks if the serial port for the arduino communication is open, and describes the issue if it isnt.
while True:
    try:
        ser = serial.Serial(port = '/dev/ttyACM0',baudrate=115200,bytesize=8)
        ser.flush()
        ser.flushInput()
        ser.reset_input_buffer()

    except serial.SerialException as var:
        print('an exception occurred',var)


    else:
        print('serial port opened')
        break


#This sets up a socket connection between the PI and the CPU tower to send Lidar distances
bufferSize = 1024

ServerPort = 2228
ServerIP = '155.31.130.196'
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP,ServerPort))
RPIsocket.setblocking(False)
socket

#Set up the data list to manipulate to plot
lidar_list = []
angle_list = []
data = {'x_values': angle_list,'y_values': lidar_list}

source = ColumnDataSource(data=data)

# create a plot using the ColumnDataSource's two columns
p = figure()
p.circle(x='x_values', y='y_values',source=source)


def callback_update_data():

    #window_size controls how many points will display
    window_size = 500;


    #flushes socket
    try:
        RPIsocket.recv(bufferSize)
    except BlockingIOError as e:
        pass
    #flush Serial
        ser.reset_input_buffer()
    #pause(.2)

    #This pulls the anlge data from the socket
    angle_line = 0
    angle_line = float(ser.readline().decode('utf-8').rstrip())


    lidar_line = 0
    try:
        message, address = RPIsocket.recvfrom(bufferSize)
        #print(message)
        readable = message.decode('utf-8')
        print(readable)
        lidar_line = float(readable)

    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError as x:
        #print(x)
        pass

    finally:
        #print('hi')
        pass

    if lidar_line != 0:


        #This controls the length of displayed data points by changing how long the list is
        #before it starts popping off data points
        if len(angle_list) >= window_size:
            angle_list.pop(0);
            angle_list.append(angle_line)
            lidar_list.pop(0);
            lidar_list.append(lidar_line)
                #print(type(data_list[0]))
            #time_list.pop(0);
            #time_list.append(time.time()-start)
            #print('at max' )
            #print(data_list)

        else:
            angle_list.append(angle_line)
            lidar_list.append(lidar_line)


        ##source.data = {'x_values': times_list,'y_values': data_list}
    source.data = {'x_values': angle_list,'y_values': lidar_list}


#This sets up your bokeh layout and updates sampling time
layout = layout([p],sizing_mode='stretch_width')

curdoc().add_root(layout)


curdoc().add_periodic_callback(callback_update_data, 1)
