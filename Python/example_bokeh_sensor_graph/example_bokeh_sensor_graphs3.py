#Kaleb Nails
#Created: 6/18/2023
#Modified:

#This is to generate a graphs in subtabs with their sub catogories
#run with: bokeh serve --show --port=5010 example_bokeh_sensor_graphs3.py

#Not all of these libraries are needed
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

import time

#This is just the list of dummy active sensors and their metrics
active_sensors = ['Alphasense','Vaisala']
sensor_variables = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
#I can just add the if loop in the for ii in active sensor like i have when I generate the tables


def which_senor_metric(name):
    if str(name) == 'Alphasense':
            print('TRUE alphasense')
            Data = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
            filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler']
            return Data, filler

    elif str(name) == 'Vaisala':
        print('PRINT TRUE VIASLA')
        Data = {'Metrics':['NO2 (ppm)','SO2 (ppm)','CO (ppm)','O3 (ppm)','PM2.5 (ug/m3)','PM10 (ug/m3)','TEMP (C)','HUM (%)','PRES (mbar)','Uptime (s)']}
        filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler','filler', 'filler','filler']
        return Data, filler

    elif str(name) == 'PurpleAir':
        Data = {'Metrics':['T_samp(s)','SFR (mL/s)','Temp (C)','RH (%)','PM_A (ug/m^3)','PM_B(ug/m^3)','PM_C (ug/m^3)']}
        filler = [ 'filler','filler', 'filler','filler','filler', 'filler','filler']
        return Data, filler
    

    
    


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
            temp_tab = Panel(child = figure(title = sense_variable), title = sense_variable)
            tabs_object[ii].tabs.append(temp_tab)
            
        #This turns all of the into scatter plots
        #below is a complicated way to generate data sources for the graphs, the format is the activesensorname_data and activesensor_source
        for ll in range(0, len(tabs_object[ii].tabs)):
            globals()[ii + '_data_tab' + str(ll)] = {'x_values':[],'y_values':[] }
            globals()[ii + '_source_tab' + str(ll)] = ColumnDataSource(data = globals()[ii + '_data_tab' + str(ll)])
            tabs_object[ii].tabs[ll].child.scatter(x = 'x_values',y = 'y_values', source = globals()[ii + '_source_tab' + str(ll)] )

        graph_and_words.children.append(tabs_object[ii])



#The only reason this block of code is here is to make generate_graph run once, this is a bad way to do it, but fine for a simple example
global counter
counter = 0 
def callback_update_data():
    global counter
    print('update:' + str(counter))
    if counter == 0:
        generate_graphs()
        counter = counter +1
    update_graphs()


def update_graphs():
    myjson = {'Sensors': 'Alphasense0', 'T_samp': 0.57, 'SFR': 3.48, 'temp': 24.4, 'RH': 47.3, 'PMA': 0.489, 'PMB': 1.535, 'PMC': 1.68}

    active_sensor_postion = 1
    for ii in active_sensors:

        #This checks to see if the sensors value is contained in the sensors list, so alphasense inside of alphasense0
        if str(ii) in myjson['Sensors']:

            
            for ll in range(0, len(myjson.keys())-1):
                global session_start_time
                new_data = {'x_values': [time.time() - session_start_time],'y_values':[list(myjson.values())[ll+1]]}

                ds_new = dict(globals()[ii + '_source_tab' + str(ll)].data)
                print('ds_new is' + str(ds_new))


                Window_max = 20
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

graph_and_words = layout([])
layout = layout([[graph_and_words]])
curdoc().add_root(layout)
curdoc().add_periodic_callback(callback_update_data, 1000)









