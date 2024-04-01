# Python Example Code Folders #


## CDP ##
This contains some clusterduck code to be run on both the micro-controller and a laptop. This was for the NASA wildfire SBIR and developing the heltec esp32 lora boards using the cluster duck protocol.
It was eventually suspected that the speed at which the bouncing occured was too slow for our applications and caused some issues. CDP slack did not have a really directly useful answer in terms of our use case.

## Camera_Code ##
I dont remember writing this, apparently this is camera code for python.

## Data_type_changing ##
For now this just has an example of how to go from a string of bytes to json, currently kind of useless with the introduction of gtp.

## Serial_Ports ##
Has some example of sending and recieving messages over socket, and then also sending floats with json etc.

## Bokeh ##
Has a ton of bokeh examples for both MOVEUAS, weather station and other research projects. The most impressive thing in here was the app I made that if you editted a matrix with the name of the sensor and what it records you could
generate whole new tables and whole new graphs. This was definately the coolest thing I did, it is completely modular and will work with any sensor systems, any amount of those sensors, and whatever differences in what they record 
and plot and make a table of it. It sounds simple but I attest it was rather complicated. Also it had to be an app with or everytime someone made a new instance of the bokeh website it they would each pull from the socket.
So every instance got every other data points. I fixed this by generating Q's and storing them on a .txt file or a .py file (I don't recall of the top of my head).

## discord bot ##
Made a discord bot that would interact with a remote PI4, I could put  "ip?" in the discord chat, and then the discord bot will respond with the Pi's Ip address. This is in case the Pi gets a new IP address. In the pis boot file it will
run something that takes its IP and puts it to a .txt and then it will run the discord bot, which then will be active on the discord server

## example_bokeh_sensor_graph ##
I don't remember exactly what this is, but I believe its a way to generate multiple tables in bokeh and the tables will all be in different tabs.

# Files #

## ard_reciever.py ##
### Real-time Data Visualization with Bokeh and Serial Communication ###

This Python script allows for real-time data visualization using Bokeh and serial communication with an Arduino device. The script reads data from the Arduino over a serial connection and plots it in a Bokeh plot, which is displayed in a web browser.

### Requirements
- Python 3.x
- Bokeh
- pyserial

### Usage
1. Connect your Arduino device to your computer.
2. Run the script using the command:
```bokeh serve --show ard_receiver.py ```
3. The Bokeh plot will open in your default web browser and display the data received from the Arduino device.

### Description
- The script initializes a serial connection with the Arduino device.
- It creates a Bokeh plot with an empty scatter plot.
- Data received from the Arduino is continuously read and plotted on the Bokeh plot in real-time.
- The plot dynamically updates as new data is received.


## measure_performance.py ##
Wonderful code that I found online that uses a decorator to report all kinds of details about a function such as consumed ram, and time it took to ran. great for optimizing

## effective_area_structs.py ##
This will take input points and their effective area of a body, give you the centriod, the shifted points, and the equation for stress and shear flow. As well as q_out-q_in for every point which you can use to solve. I also have a matlab version

## effective_area_structs_fromC.py ##
This is the same as effective_area_structs.py, but it starts you of from if you are given your centriod and shifted points already

