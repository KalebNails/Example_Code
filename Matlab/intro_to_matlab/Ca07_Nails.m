

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA07
% PROGRAM PURPOSE: to find the average temp over time and use a function to
% read it
% AUTHOR: Kaleb Nails
% DATE: 2/15/22
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Clear workspace and command window
clear, clc

% STEP 1: DEFINE THE PROBLEM
% Daily Temperature Average
% Program reads data from file, calculates temp. average, plots temps vs
% time
 
% GIVENS: Temperature and time data (Excel file) 
% FIND: Average temperature AND Plot temp.vs time

% Getting data from file:

% Store name of data file in variable filename
% This step is not necessary but it makes the program more flexible


%Use the function to read the filename for the project
filename = input('What is the name of the file: ','s');
File = readXLFile(filename);
 
% In order to calculate the average, we need the temperature data
% All data from the file was imported as one matrix; 
% therefore, some data preparation is
% needed before we can perform the calculation

% Extract temperature data from File, store in variable "temps"
% The temp data is located in column 2 of tempData
temps = File(:,2);

% Extract time data from File, store in variable "hours"
% The time data is located in column 1 of tempData
hour = File(:,1);

% STEP 2: DIAGRAMS (NOT APPLICABLE)

% STEP 3: THEORY
% To calculate the average of a dataset, we must add all elements and then
% divide the sum by the size of the dataset (number of elements)

% STEP 4: ASSUMPTIONS
% Not needed here, this is a very simple problem

% STEP 5: SOLUTION STEPS
% Calculates temperature average by adding all elements and diving 
% by number of elements 
% tempsAve = sum(temps)/numel(temps);

% A more efficient way is to use MATLAB library function mean()
tempsAve = mean(temps);

% STEP 6: IDENTIFY RESULTS
% Display result (average daily temperatures)
fprintf('The average daily tempuratures in F is %.2f \n',tempsAve)
 
% Display daily temperature chart - plot(x,y)
plot(hour,temps)
title ('Daily Tempuratures')
xlabel('Hours')
ylabel('Temps (F)')
