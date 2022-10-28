#Kaleb Nails
#
# Created: 10/28/22
# Modified: 10/28/2022
#Purpose: Will print which radio button was pushed on a live bokeh server

# To run:  bokeh serve --show Bokeh_Server_Button_Input.py



from bokeh.models import RadioGroup
from bokeh.io import curdoc

#Radio handler is just the function that is called when a button is selected, the new is just which button was selected in this case
def radio_handler(new):
    print('Radio button option' + str(new) + ' selected.')

#This defines your button, there are many other types in the bokeh documention.
radio_group = RadioGroup(labels = ["Option1","Option2"], active =0)
radio_group.on_click(radio_handler)

curdoc().add_root(radio_group)