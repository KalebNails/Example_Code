#Kaleb Nails
#
#Created: 10/18/2022
#Last Modification: 10/18/2022
#
#
# Makes a bokeh local website that updates

#Note to self, save before hitting run each time, or it won't save the code
#To run as a server use boka serve ####.py
#to display run adn display boka serve ####.py --show
#bokeh serve --show .\bokeh_website_example.py --check-unused-sessions 1000 

from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.io import curdoc
global x 
x=1
y=2


#first you create a figure named plot
plot = figure(title = 'simple example')
plot.circle([1,2], [3,4])

plot2 = figure(title = 'simple example')
plot2.circle([x,y], [3,4])

#curdoc is the key to updating the webpage
def update():
    global x
    x = x + 1
    
    plot2.circle([x,y], [3,4])
    
    


curdoc().add_root(plot)
curdoc().add_root(plot2)
curdoc().add_periodic_callback(update, 1000)
curdoc().title = "Using the Bokeh Server"






# import numpy as np
# from bokeh.io import curdoc
# from bokeh.layouts import row, column
# from bokeh.models import ColumnDataSource
# from bokeh.models.widgets import Slider, TextInput
# from bokeh.plotting import figure
# N = 200
# x = np.linspace(0, 4*np.pi, N)
# y = np.sin(x)
# source = ColumnDataSource(data = dict(x = x, y = y))
# plot = figure(plot_height = 400, plot_width = 400, title = "sine wave")
# plot.line('x', 'y', source = source, line_width = 3, line_alpha = 0.6)
# freq = Slider(title = "frequency", value = 1.0, start = 0.1, end = 5.1, step = 0.1)
# def update_data(attrname, old, new):
#    a = 1
#    b = 0
#    w = 0
#    k = freq.value
#    x = np.linspace(0, 4*np.pi, N)
#    y = a*np.sin(k*x + w) + b
#    source.data = dict(x = x, y = y)
# freq.on_change('value', update_data)
# curdoc().add_root(row(freq, plot, width = 500))
# curdoc().title = "Sliders"



