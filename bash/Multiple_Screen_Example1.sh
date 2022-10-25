#// Kaleb Nails
#// Created: 10/2/2022
#//Modified: 10/25/2022
#//
#//


#// to run use chmod +x, dont forget. chmod gives it executable permission. then run with ./
#// screen
#// cd Python\ code\ folder/ 

#chmod +x .CDP_JSON_Reciever.py
#!/bin/bash
echo "Hello World"
echo "USER IS $USER"

#This gives the file permission to run
chmod +x CDP_JSON_Float_Reciever.py

#The dms opens a detaached screen then -x stuff brings it to be typed into the command line the echo simulates pressing a space bar
#The purpose of screen is to open different console of the main one. You can deatach and reattach your scene which will "save" where you were. 
#This also allows you to maintain an SSH connection where it normally could be interupted. I could SSH into a remote unix shell, detatch it and
#move and I could still access the shell.

# $(echo) is to simulate hitting return
screen -dmS alpha1
screen -r alpha1 -X stuff "python3 CDP_JSON_Float_Reciever.py"$(echo -ne '\015')

screen -dmS alpha2
screen -r alpha2 -X stuff "python3 CDP_JSON_Float_Reciever.py"$(echo -ne '\015')