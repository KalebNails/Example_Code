
import socket
import time

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

bufferSize = 1024

ServerPort = 2228
ServerIP = '155.31.130.196'
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP,ServerPort))
RPIsocket.setblocking(False)
socket


data_list = []
times_list = []

#data = {'x_values': data_list,'y_values': times_list}
start=time.time()
data = {'x_values': times_list,'y_values': data_list}

source = ColumnDataSource(data=data)

# create a plot using the ColumnDataSource's two columns
p = figure()
p.circle(x='x_values', y='y_values',source=source)


def callback_update_data():
#while True:
    line = 0
    try:
        message, address = RPIsocket.recvfrom(bufferSize)
        #print(message)
        readable = message.decode('utf-8')
        print(readable)
        line = float(readable)

    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError as x:
        #print(x)
        pass

    finally:
        #print('hi')
        pass



    try:
        message, address = RPIsocket.recvfrom(bufferSize)
        #print(message)
        readable = message.decode('utf-8')
        print(readable)
        line = float(readable)

    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError as x:
        #print(x)
        pass

    finally:
        #print('hi')
        pass

        #print(line)



        if len(data_list) >= 500:
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
        #print('tesing!!!!!!!!!')
        source.data = {'x_values': times_list,'y_values': data_list}
        #print('hi')


        #print(data_list)
        #print(times_list)
        #print('tesing')
        source.data = {'x_values': times_list,'y_values': data_list}




layout = layout([p],sizing_mode='stretch_width')

curdoc().add_root(layout)


curdoc().add_periodic_callback(callback_update_data, 10)
