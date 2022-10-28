#Kaleb Nails
#
# Created: 10/28/22
# Modified: 10/28/2022
#Purpose: Will print which check boxes was pushed on a live bokeh server. and update the code and bokeh server in response

# To run:  bokeh serve --show Bokeh_Server_Checkbox_example.py  
from bokeh.models import CheckboxGroup
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models.widgets import Div


selected = Div(background='lightskyblue' , width=800, text="""None Selected yet""", render_as_text=True)

#Radio handler is just the function that is called when a button is selected, the new is just which button was selected in this case
def radio_handler(new):
    print('Radio button option' + str(new) + ' selected.')
    message = []
    list = []

    #This entire for is just to print the name above the check box
    #This should work with any number of sensors
    for i in new:
        message.append(box_group.labels[i] + ', ')
    #print(message)
    #print("".join(message))
    selected.text = "".join(message)
    if not selected.text:
        selected.text =  "None Selected yet"


#This defines your button, there are many other types in the bokeh documention.
#you can change labels and it should work
box_group = CheckboxGroup(labels = ["OPC","PurpleAir","SPS-30"], active =[])
box_group.on_click(radio_handler)

#This adds the root to the button
layout = layout([   [selected],
              [box_group]],sizing_mode='stretch_width')

curdoc().add_root(layout)