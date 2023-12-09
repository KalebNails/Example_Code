#Kaleb Nails
#
# Created: 11/1/22
# Modified: 2/3/2023
#Purpose: Live stream data to anyone who needs to see it
  

# To run:  bokeh serve --show Test_file.py  
# To run over wifi: bokeh serve --show .\Test_app\ --allow-websocket-origin=10.33.142.235:5006
# bokeh serve --show .\Test_app\
from unicodedata import name
from bokeh.models import CheckboxGroup, CheckboxButtonGroup, ColumnDataSource, TableColumn, DataTable, Select
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models.widgets import Div, Tabs, Panel
from bokeh.models import ColumnDataSource, TableColumn, DataTable
from bokeh.plotting import figure


import pandas as pd

from datetime import datetime
import json

import Pull_Socket_Data 
import config

import time


#These variables are involved with preventing the checkboxes from being changed when locked
global Variable_Lock
global Previous_Sensor

Variable_Lock = []
Lock_Vars_Name = ['Lock Parameters']
selected = Div(background='lightskyblue' , width=800, text="""None Selected yet""", render_as_text=True)

#This creates uptime boxes
current_time_display = Div(background = 'lightgreen',width=1400,text="""Time-unstarted""", render_as_text=True)
up_time_display = Div(background = 'crimson',width = 1000,text="""Bokeh-uptime-blank""", render_as_text=True)
last_data_time_display = Div(background = 'slateblue',width = 1000,text="""last-data-recieved""", render_as_text=True)



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
    generate_graphs()
    

    



#this is the function that generates graphs

def generate_graphs():
    

    global active_sensors
    global session_start_time 
    session_start_time= time.time()
    #global sensor_variables

    #It is nessesary to make an empty tab objects before hand so we can assign it empty values
    #It also empties out the layout in case if children need to be remade
    tabs_object = {}
    graph_and_words.children = []
    
    for ii in active_sensors:

        

        #This creates an empty space in the tabs_object dictionary so that it can later be filled
        tabs_object[ii] = {}
        tabs_object[ii]['tabs'] = []
        
        #This creates the text above that labels it
        selected_sensor = Div(background='lightskyblue' , width=800, text=ii, render_as_text=True)
        graph_and_words.children.append(selected_sensor)

        #Creates an empty tabs object to fill later
        tabs_object[ii] = Tabs(tabs = [])


        print('ii' + ii)
        sensor_variables, _  = which_senor_metric(ii)

        #This loops through each provided metric you want to graph
        for sense_variable in sensor_variables['Metrics']:

            #This creates the a tab and attaches it to the list of current tabs
            temp_tab = Panel(child = figure(title = sense_variable, sizing_mode="scale_width", height = 100), title = sense_variable)
            tabs_object[ii].tabs.append(temp_tab)
            
        #This turns all of the into scatter plots
        #below is a complicated way to generate data sources for the graphs, the format is the activesensorname_data and activesensor_source
        for ll in range(0, len(tabs_object[ii].tabs)):
            globals()[ii + '_data_tab' + str(ll)] = {'x_values':[],'y_values':[] }
            globals()[ii + '_source_tab' + str(ll)] = ColumnDataSource(data = globals()[ii + '_data_tab' + str(ll)])
            tabs_object[ii].tabs[ll].child.line(x = 'x_values',y = 'y_values', source = globals()[ii + '_source_tab' + str(ll)] )

        graph_and_words.children.append(tabs_object[ii])





def which_senor_metric(name):
    if str(name) == 'Alphasense':
            print('TRUE alphasense')
            Data = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
            filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler']
            return Data, filler

    elif str(name) == 'Vaisala':
        print('PRINT TRUE VIASLA')
        Data = {'Metrics':['NO2 (ppm)','SO2 (ppm)','CO (ppm)','O3 (ppm)','PM2.5 (ug/m3)','PM10 (ug/m3)','TEMP (C)','HUM (%)','PRES (mbar)']}
        filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler','filler', 'filler']
        return Data, filler

    elif str(name) == 'PurpleAir':
        Data = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
        filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler']
        return Data, filler






def generate_tables():
    global active_sensors
    Tables.children.clear()
    #This creates your left most Variable column
    Data = {'Metrics':['Time:','Humidity','Temp']}
    #This is a general place holder
    filler = [ 'fillertime','fillerhumid', 'fillertemp']
    for i in active_sensors:
        name = i

        #This is a function that returns the column variables and a filler variable that just is used when initially generating the tables
        Data, filler = which_senor_metric(name)
                #message = {"Sensor":"Purpleair0","date":row[0],"cnt":row[1], 'T_samp': row[2], "SFR": row[3], "temp": row[4], "RH": row[5], "PMA":row[6],"PMB":row[7],"PMC":row[8]}





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
        #This tries to pull from the Q of the invididual session
        #print(str(curdoc().session_context._id))
        Pull_Socket_Data.update_queues()
        readable = config.dict_queues[str(curdoc().session_context._id)].pop(0)
        print('printing readable: ' + str(readable))


        
        #reads the incoming data, and transforms that into a python dictionary

        myjson = json.loads(readable)
         
        if myjson['Sensors'][0:6] == 'ttyACM':
            myjson['Sensors'] = 'Alphasense' + myjson['Sensors'][6]

        print('printing myjson: ' + str(myjson))
        # I am very very very lazy and this is an awful way to iterate through each message to figure out which
        #child is the proper table
        global active_sensors
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
                last_data_time = datetime.now()
                last_data_time_display.text = 'Uptime: {0}'.format(str(last_data_time).split('.')[0])
            except:
                pass
        update_graphs(myjson)

    #when recvfrom blocking is false it will return this error when the buffer is empty
    except BlockingIOError as error:
        #print(error)
        print('Blockingioerror')
        
    except OSError as error:
        #print(error)
        print('OSerror')
        
    except ValueError:
        print('json decoder mistake')
    except IndexError:
        #print('Pop maybe decoder mistake, fix this later')
        pass
    
    
    current_time = datetime.now()
    current_time_display.text = 'Currently: {0} '.format(current_time.strftime("%c"))
    up_time_display.text = 'Uptime: {0}'.format(str(current_time - config.t0).split('.')[0])

    



def update_graphs(myjson):
    #myjson = {'Sensors': 'Alphasense0', 'T_samp': 0.57, 'SFR': 3.48, 'temp': 24.4, 'RH': 47.3, 'PMA': 0.489, 'PMB': 1.535, 'PMC': 1.68}
    global active_sensors
    active_sensor_postion = 1
    for ii in active_sensors:

        #This checks to see if the sensors value is contained in the sensors list, so alphasense inside of alphasense0
        if str(ii) in myjson['Sensors']:

            
            for ll in range(0, len(myjson.keys())-1):
                global session_start_time
                new_data = {'x_values': [time.time() - session_start_time],'y_values':[list(myjson.values())[ll+1]]}

                ds_new = dict(globals()[ii + '_source_tab' + str(ll)].data)
                print('ds_new is' + str(ds_new))

                #Window_max controls how many points you have on the screen at once
                Window_max = 40
                print('the number of points on the screen is:' + str(len(list(ds_new.values())[0])))
                if len(list(ds_new.values())[0]) < Window_max:
                    ds_new['x_values'].append(new_data['x_values'][0])
                    ds_new['y_values'].append(new_data['y_values'][0])
                    #IF you wanted to add color per sensor just append sensor value as well, this would be based on the following number in the sensors value in the dict json
                else:
                    
                    ds_new['x_values'].pop(0)
                    ds_new['y_values'].pop(0)
                    ds_new['x_values'].append(new_data['x_values'][0])
                    ds_new['y_values'].append(new_data['y_values'][0])


                print(globals()[ii + '_source_tab' + str(ll)].data)
                globals()[ii + '_source_tab' + str(ll)].data = ds_new

        print((graph_and_words.children[1]))

        #increment active sensor position by 2, because in the children it goes [Div,tab,div,tabs], so this ensures you work with the tabs
        active_sensor_postion = active_sensor_postion + 2


#This creates an empty space for the tables to exist
down_menus = layout([])
Tables = layout([])
graph_and_words = layout([])

layout = layout([   [current_time_display], [up_time_display],[last_data_time_display], [selected],
              [box_group, down_menus], [Lock_Button],[Tables],[graph_and_words]],sizing_mode='stretch_width')



curdoc().add_root(layout)
curdoc().add_periodic_callback(callback_update_data, 100)


#new plane for I in active sensors
#use Div to label
#then generate tabs based on metrics
#The figure out how to populate the data

#This is what alphasense input data will look like
#{ "Sensors":"ttyACM0", "T_samp (s)" : "0.570" , "SFR (mL/s)":"4.000",  "Temp (C)":"26.8" ,  "RH (%)":"42.7",  "PM_A (ug/m^3)":"0.685",  "PM_B(ug/m^3)" : "1.409",  "PM_C (ug/m^3)":"1.409" }


#This is what visala input data will look like 
# {"Sensor":"Vaisala,"NO2 (ppm)":"       0.009",  "SO2 (ppm)":"       0.023",  "CO (ppm)":"       0.738",  "O3 (ppm)":"       0.001",  "PM2.5 (ug/m3)":"       0.500",  "PM10 (ug/m3)":"        4.50",  "TEMP (C)":"   21.20",  HUM (%):"    60.4",  PRES (mbar):"   1017.80",  "Uptime (s)":   594156.00,  "Validity":True}