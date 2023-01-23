#Kaleb Nails
#
# Created: 11/1/22
# Modified: 1/23/2023
#Purpose: Create uses bokeh server to create a certain number of tables 
# of user desided sizes live. THERE IS AN ISSUE WITH THIS CURRENTLY. It also
# could be greatly condensed and optimized.  

# To run:  bokeh serve --show Test_file.py  
# To run over wifi: bokeh serve --show --allow-websocket-origin=10.33.000.000:5006 Test_file.py
from unicodedata import name
from bokeh.models import CheckboxGroup, CheckboxButtonGroup, ColumnDataSource, TableColumn, DataTable, Select
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models.widgets import Div
from bokeh.models import ColumnDataSource, TableColumn, DataTable 

import pandas as pd

import socket
from datetime import datetime
import json
#This is for ethernet connection
bufferSize = 1024
#time server was created
t0 = datetime.now()

#This is the IP of the laptop. If it wasn't in a try and failed it would crash the entire bokeh server
try:
    ServerPort = 2222
    ServerIP = '169.254.26.44'
    RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    RPIsocket.bind((ServerIP,ServerPort))
    RPIsocket.setblocking(False)
except:
    print('No eithernet has been connect. Please connect before boot-up for live data')
    pass

#These variables are involved with preventing the checkboxes from being changed when locked
global Variable_Lock
global Previous_Sensor

Variable_Lock = []
Lock_Vars_Name = ['Lock Parameters']
selected = Div(background='lightskyblue' , width=800, text="""None Selected yet""", render_as_text=True)

#This creates uptime boxes
current_time_display = Div(background = 'lightgreen',width=1400,text="""Time-unstarted""", render_as_text=True)
up_time_display = Div(background = 'crimson',width = 1000,text="""Bokeh-uptime-blank""", render_as_text=True)

#Radio handler is just the function that is called when a button is selected, the new is just which button was selected in this case

def radio_handler(new):
    global Previous_Sensor
    #This if checks if the variables are locked
    if not Variable_Lock:
        
        print('Radio button option' + str(new) + ' selected.')
        message = []
        list = []
        
        Previous_Sensor = new
        #This entire for is just to print the name above the check box
        #This should work with any number of sensors

        #down_menus.children.append(drop_down)
        
        down_menus.children.clear()
        for i in new:
            message.append(box_group.labels[i] + ', ')
            temp_drop = Select(title= str(box_group.labels[i]) ,  value = "1", height_policy = "min", options=DropD_Menu)
            temp_drop.on_change("value", dropdown_callback)
            down_menus.children.append(temp_drop)
            

            
        reset_active_buttons()
            
            
            #down_menus.children.append(Select(title= box_group.labels[i] ,  value = "foo", height_policy = "min", options=DropD_Menu))
        

        #print(message)
        #print("".join(message))
        selected.text = "".join(message)
        if not selected.text:
            selected.text =  "None Selected yet"
            down_menus.children.clear
            


    else:
        #Prints an error messages and change the textboxes back to the originally checked ones
        print('Variable locked or error has occured')
        Charecter_Holder = selected.text
        selected.text =  "Variable Locked! Sensor selected are " + Charecter_Holder
        box_group.active = Previous_Sensor
        global active_sensors
        
        #for i in down_menus.children:
            #i.value = 'locked'
        
        
        
def dropdown_callback(attr, old,new):
    #print(str(old))
    #print(str(new))
    #print(str(attr))
    
    reset_active_buttons()

    #print(str(down_menus.children[0].title))
    #print(str(down_menus.children[0].value))
    
    
def reset_active_buttons():
    global active_sensors
    active_sensors = {}
    for i in down_menus.children:
        active_sensors[str(i.title)] = i.value  
    print(active_sensors) 
 
    
    

#This defines your button, there are many other types in the bokeh documention.
#you can change labels and it should work
box_group = CheckboxGroup(labels = ["OPC","Alphasense","PurpleAir","SPS-30","pms5003","Vaisala"], active =[])
box_group.on_click(radio_handler)

#This sets up the drop down menu
DropD_Menu = [("1", "1"), ("2", "2"),("3", "3")]
#drop_down = Dropdown(label="Dropdown button", height_policy = "max", menu=DropD_Menu)

#This function is what is called up on the onclick, it sets the variable to lock the checkboxes
def Lock_Button_handler(new):
    #print('button')
    print(new)
    global Variable_Lock
    Variable_Lock = new
    
    Tables.children.clear

    
    generate_tables()



def generate_tables():
    global active_sensors
    Tables.children.clear()
    #This creates your left most Variable column
    Data = {'Metrics':['Time:','Humidity','Temp']}
    #This is a general place holder
    filler = [ 'fillertime','fillerhumid', 'fillertemp']
    for i in active_sensors:
        name = i

        #This is extremely tedious to make, but follow the format and it should work. if you add any new sensors just add them by following 
        #the format below
        if name == 'Alphasense':
            Data = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
            filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler']
        elif name == 'Vaisala':
            Data = {'Metrics':['NO2 (ppm)','SO2 (ppm)','CO (ppm)','O3 (ppm)','PM2.5 (ug/m3)','PM10 (ug/m3)','TEMP (C)','HUM (%)','PRES (mbar)','Uptime (s)']}
            filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler','filler', 'filler','filler']




        columns_A = [TableColumn(field='Metrics', title='Metrics')]

        for t in range(0,int(active_sensors[i])):
            Data[name+ str(t)] = filler
            columns_A.append(TableColumn(field = name+ str(t) , title = name+ str(t)))


        df = pd.DataFrame(Data)

        source = ColumnDataSource(df) # cds is a dict with 'index' and keys as column headings

        myTable = DataTable(source=source, columns=columns_A)  
        print(myTable.id) 
        Tables.children.append(myTable)

    #print((Tables.children))
    #print((Tables.children[0]))
    #print((Tables.children[0].source.data))
    #print((Tables.children[1].source.data))
    #ds_new = dict(Tables.children[0].source.data)
    #ds_new['PurpleAir0'][1] = 3
    #Tables.children[0].source.data = ds_new

#This defines the lock button
Lock_Button = CheckboxButtonGroup(labels = Lock_Vars_Name, active = [])
Lock_Button.on_click(Lock_Button_handler)

###### If you want to add update time, add a time column at the top, then increase the starting count by 1 and just manuelly set that one
#to be the most current time, so 0 would just be time
def callback_update_data():
    
    try:
        #reads the incoming data, and transforms that into a python dictionary
        message, address = RPIsocket.recvfrom(bufferSize)
        readable = message.decode('utf-8')
        
        #print(readable)
        

        myjson = json.loads(readable)
        
        if myjson['Sensors'][0:6] == 'ttyACM':
            myjson['Sensors'] = 'Alphasense' + myjson['Sensors'][6]

        print(myjson)
        # I am very very very lazy and this is an awful way to iterate through each message to figure out which
        #child is the proper table
        
        for i in range(0,len(active_sensors)):
            try:
                ds_new = dict(Tables.children[i].source.data)
                
                
                #the 1 just decides which row, this can be changed later!!!
                ########### Here it basically checks if the Sensor field exists within that particular table and then changes the values
                #myjson['Sensor'] will not exist in ds_new if it is the wrong sensor, this is how it goes through each sensor
                #ds_new[myjson['Sensors']][1] = myjson['value']


                #This iterates through each row changing the number
                counter = 0
                for ii in myjson:
                    try:
                        print(myjson[ii])
                        #print(ds_new[myjson['Sensors']][counter])
                        ds_new[myjson['Sensors']][counter] = myjson[ii]
                        print('______________')
                        print(ii)
                        print(myjson['Sensors'])
                        #This prevents it from printing the name of the sensor in the first row
                        if str(ii) != 'Sensors':
                            counter += 1
                    except:
                        pass

                Tables.children[i].source.data = ds_new
            except:
                pass

    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError as error:
        print(error)
        pass
    except OSError as error:
        print(error)
        pass

    current_time = datetime.now()
    current_time_display.text = 'Currently: {0} '.format(current_time.strftime("%c"))
    up_time_display.text = 'Uptime: {0}'.format(str(current_time - t0).split('.')[0])




#This creates an empty space for the tables to exist
down_menus = layout([])
Tables = layout([])


layout = layout([   [current_time_display], [up_time_display], [selected],
              [box_group, down_menus], [Lock_Button],[Tables]],sizing_mode='stretch_width')

curdoc().add_root(layout)
curdoc().add_periodic_callback(callback_update_data, 1000)


#This is what alphasense input data will look like
#{ "Sensors":"ttyACM0", "T_samp (s)" : "0.570" , "SFR (mL/s)":"4.000",  "Temp (C)":"26.8" ,  "RH (%)":"42.7",  "PM_A (ug/m^3)":"0.685",  "PM_B(ug/m^3)" : "1.409",  "PM_C (ug/m^3)":"1.409" }


#This is what visala input data will look like 
# {"Sensor":"Vaisala,"NO2 (ppm)":"       0.009",  "SO2 (ppm)":"       0.023",  "CO (ppm)":"       0.738",  "O3 (ppm)":"       0.001",  "PM2.5 (ug/m3)":"       0.500",  "PM10 (ug/m3)":"        4.50",  "TEMP (C)":"   21.20",  HUM (%):"    60.4",  PRES (mbar):"   1017.80",  "Uptime (s)":   594156.00,  "Validity":True}
