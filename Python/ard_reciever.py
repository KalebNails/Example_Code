
import serial #This is from pyserial
import time

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

#This checks if the port is open, and describes the issue if it isnt.
while True:
    try:
        ser = serial.Serial(port = '/dev/ttyACM0',baudrate=9600,bytesize=8)
        ser.flush()
        ser.flushInput()
        ser.reset_input_buffer()

    except serial.SerialException as var:
        print('an exception occurred',var)


    else:
        print('serial port opened')
        break

data_list = []
times_list = []

#data = {'x_values': data_list,'y_values': times_list}
start=time.time()
data = {'x_values': times_list,'y_values': data_list}

source = ColumnDataSource(data=data)

# create a plot using the ColumnDataSource's two columns
p = figure()
p.circle(x='x_values', y='y_values',source=source,size=5, color='red', alpha=0.5 )


def callback_update_data():
#while True:
    ser.flush()
    window_size = 2000
    line = 0
    line = float(ser.readline().decode('utf-8').rstrip())
    if ser.in_waiting > 0:
        line = float(ser.readline().decode('utf-8').rstrip())

        print(line)



        if len(data_list) >= window_size:
            data_list.pop(0);
            data_list.append(line)
                #print(type(data_list[0]))
            times_list.pop(0);
            times_list.append(time.time()-start)
            #print('at max' )
            #print(data_list)

        else:
            data_list.append(line)
            times_list.append(time.time()-start)
            #print('growing: ' + str(len(data_list)))

        #print(data_list)
        #print(times_list)
        #print('!')
        source.data = {'x_values': times_list,'y_values': data_list}
        #print('hi')
    else:

        if len(data_list) >= window_size:
            data_list.pop(0);
            data_list.append(line)
            #print(type(data_list[0]))

            times_list.pop(0);
            times_list.append(time.time()-start)

            #print(data_list)

        else:
            data_list.append(line)
            times_list.append(time.time()-start)
            #print('growing: ' + str(len(data_list)))

        #print(data_list)
        #print(times_list)
        #print('tesing')
        source.data = {'x_values': times_list,'y_values': data_list}



layout = layout([p],sizing_mode='stretch_width')

curdoc().add_root(layout)


curdoc().add_periodic_callback(callback_update_data, 5)
