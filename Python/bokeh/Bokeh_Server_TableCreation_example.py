#Kaleb Nails
#
# Created: 11/1/22
# Modified: 11/1/2022
#Purpose: To create bokeh table that changes with size from hardcoded variables

# To run:  bokeh serve --Bokeh_Server_TableCreation_example.py  
from bokeh.models import CheckboxGroup, CheckboxButtonGroup, ColumnDataSource, TableColumn, DataTable
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models.widgets import Div

import pandas as pd


#this dictates how many columns
sensor_count = 5

#This will change the name of the sensor
name = 'SPS'
#This creates your left most Variable column
Data = {'Metrics':['Time:','Humidity','Temp']}
#This is a general place holder
filler = [ 'time1222','humidity1222', 'temp1222']
#This sets up the variable column
columns_A = [TableColumn(field='Metrics', title='Metrics')]

#This adds new dicts inside of data
for i in range(0,sensor_count):
    Data[name+ str(i)] = filler
    columns_A.append(TableColumn(field = name+ str(i) , title = name+ str(i)))


df = pd.DataFrame(Data)

source = ColumnDataSource(df) # cds is a dict with 'index' and keys as column headings

myTable = DataTable(source=source, columns=columns_A)

curdoc().add_root(myTable)