from bokeh.models import Div
from bokeh.io import curdoc
from bokeh.models.widgets import Panel


Sub_textbox = Div(text='hello how are you',width=500,height=200)

def graph_update(): 
    Sub_textbox.text = 'Im SOOOOO goated'


Graph_Sub_Page = curdoc()
Graph_Sub_Page.add_root(Sub_textbox)

Graph_Sub_Tab = Panel(child = Graph_Sub_Page,title = 'tab 2')

