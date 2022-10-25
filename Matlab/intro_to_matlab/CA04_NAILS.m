%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA04
% PROGRAM PURPOSE: Simulate data collected on senesor based on user inputs
% of the highest value the lowest value and its size
% AUTHOR: Kaleb Nails
% DATE: 1/27/2022
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%{
 Simulate information collected from a set of sensors (3) taken during a
 specified period of time (seconds).
 Each row contains a set of sensor readings, with the first row containing
 values collected at 0 seconds, the second row containing values collected at
 1.0 seconds, and so on.
 User chooses sensor value range and dataset size. 
 
 Find both the maximum value and the minimum value recorded on
 each sensor and determine at what times they occurred.
 
 Display results.
 %}
% Clear workspace and command window
 clc, clear
% STEP 1: DATA INPUT
% Need: sensor1, sensor2, sensor3, and time in seconds
% GENERATE SENSOR DATA
%*****************************************************
% Request sensor data range from user
fprintf('*** SENSOR DATA SIMULATOR***\n')
fprintf('****************************\n')
name = input('Please enter the scientists name: ','s');
Highrange = input('Enter the highest Desired Senor Value: ');
Lowrange = input('Enter the lowest Desired Senor Value: ');
Setsize = input('Enter the size of the data set: ');
% Request size of dataset from user (how many elements to generate)
% Generate sensor datasets as per user input 
Sensor1 = rand(1,Setsize)*(Highrange - Lowrange) + Lowrange;
Sensor2 = rand(1,Setsize)*(Highrange - Lowrange) + Lowrange;
Sensor3 = rand(1,Setsize)*(Highrange - Lowrange) + Lowrange;


% Generate time vector (seconds)
t = 1:1:Setsize;
clc
% ******************************************************
% FIND MINIMUM AND MAXIMUM VALUES FOR EACH SENSOR
% Find the minimum reading in all 3 sensors, and corresponding time of
% occurrence
Minsens1 = min(Sensor1');
WhereMin1 = find(Sensor1==Minsens1);
Minsens2 = min(Sensor2');
WhereMin2 = find(Sensor2==Minsens2);
Minsens3 = min(Sensor3');
WhereMin3 = find(Sensor3==Minsens3);
% Find the maximum readinhelg in all 3 sensors, and corresponding time of
% occurrence

%NOTE TO SELF YOU CAN ALSO USE [vlaue, where] = min(Sensor1) and that is
%easier and saves lines
MAXsens1 = max(Sensor1');
WhereMAX1 = find(Sensor1==MAXsens1);
MAXsens2 = max(Sensor2');
WhereMAX2 = find(Sensor2==MAXsens2);
MAXsens3 = max(Sensor3');
WhereMAX3 = find(Sensor3==MAXsens3);
% ******************************************************
% DISPLAY RESULTS
% Results for sensor 1
fprintf('\n %ss data\n',name)
fprintf('\n***SENSOR 01***\n')
fprintf('The maximum value for sensor 01 is %.2f and occurs at %.1f seconds ', MAXsens1,WhereMAX1)
fprintf('\n The minimum value for sensor 01 is %.2f and occurs at %.1f seconds ', Minsens1,WhereMin1)
 % Results for sensor 2
fprintf('\n***SENSOR 02***\n')
fprintf('The maximum value for sensor 02 is %.2f and occurs at %.1f seconds ', MAXsens2,WhereMAX2)
fprintf('\n The minimum value for sensor 02 is %.2f and occurs at %.1f seconds ', Minsens2,WhereMin2)
% Results for sensor 3
fprintf('\n***SENSOR 03***\n')
fprintf('The maximum value for sensor 01 is %.2f and occurs at %.1f seconds ', MAXsens3,WhereMAX3)
fprintf('\n The minimum value for sensor 01 is %.2f and occurs at %.1f seconds ', Minsens3,WhereMin3)
% *********************************************************
% PORGRAM EXIT MESSAGE
fprintf('\n****************************\n')
fprintf('****************************\n')
% *********************************************************