#Kaleb Nails
#
# Created: 10/28/22
# Modified: 10/28/2022
#Purpose: To create a check box button system that can be locked

# To run:  bokeh serve --show Bokeh_Server_Checkbox_example2.py  
from bokeh.models import CheckboxGroup, CheckboxButtonGroup
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models.widgets import Div

#These variables are involved with preventing the checkboxes from being changed when locked
global Variable_Lock
global Previous_Sensor

Variable_Lock = []
Lock_Vars_Name = ['Lock Parameters']
selected = Div(background='lightskyblue' , width=800, text="""None Selected yet""", render_as_text=True)

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
        for i in new:
            message.append(box_group.labels[i] + ', ')
        #print(message)
        #print("".join(message))
        selected.text = "".join(message)
        if not selected.text:
            selected.text =  "None Selected yet"

    else:
        #Prints an error messages and change the textboxes back to the originally checked ones
        print('Variable locked or error has occured')
        Charecter_Holder = selected.text
        selected.text =  "Variable Locked! Sensor selected are " + Charecter_Holder
        box_group.active = Previous_Sensor

#This defines your button, there are many other types in the bokeh documention.
#you can change labels and it should work
box_group = CheckboxGroup(labels = ["OPC","PurpleAir","SPS-30"], active =[])
box_group.on_click(radio_handler)

#This function is what is called up on the onclick, it sets the variable to lock the checkboxes
def Lock_Button_handler(new):
    #print('button')
    #print(new)
    global Variable_Lock
    Variable_Lock = new

#This defines the lock button
Lock_Button = CheckboxButtonGroup(labels = Lock_Vars_Name, active = [])
Lock_Button.on_click(Lock_Button_handler)

#This adds the root to the button
layout = layout([   [selected],
              [box_group], [Lock_Button]],sizing_mode='stretch_width')

curdoc().add_root(layout)