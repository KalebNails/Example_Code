%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: In-Class Activity #2
% PROGRAM PURPOSE: Find the average low and high temp from a city and
% display this both in a graph
% AUTHOR:Kaleb Nails
% DATE: 1/20/22
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc

% STEP 1: DEFINE THE PROBLEM
% Monthly Temperature Average
% Program reads data from file
 
% GIVENS: Temperature and time data and raindata (Excel file) 
% FIND: Average low and high temperature AND Plot temp.vs time

% Extract data from Excel file, store in variable "tempData"
% Note that ONLY NUMERIC DATA is retrieved
tempData = readmatrix('DBMonthlyTemps.xlsx');
 
% In order to calculate the average, we need the temperature data
% All data from the file was imported as one matrix; 
% therefore, some data preparation is
% needed before we can perform the calculation

% Extract temperature data from tempData, store in variable "high" or "low"
% The temp data is located in column 2 and 3 of tempData, 2 is lows and 3
% is highs
high = tempData(:,2);
low = tempData(:,3);

% STEP 3: THEORY
% To calculate the average of a dataset, we must add all elements and then
% divide the sum by the size of the dataset (number of elements)

% STEP 4: ASSUMPTIONS
% Not needed here, this is a very simple problem

% STEP 5: SOLUTION STEPS
% Calculates temperature average by adding all elements and dividing 
% by number of elements or use mean function

%Gives the high average temps of the data set
highAve = mean(high);
%Gives the low average temps of the data set
lowAve = mean (low);

% STEP 6: IDENTIFY RESULTS
% Display result (average monthly temperatures)
fprintf('The high monthly average tempurature in F is %.1f \n',highAve)
fprintf('The low monthly average tempurature in F is %.1f \n',lowAve)

%This creates a list of numbers from 1 to the amount of months 
% temperatures where recorded in the original excel files
months = (1:1:numel(high));

% Display daily temperature chart - plot(x,y)
%use help plot to find more about the linetypes and colors
plot(months,high,'red')

%hold on ensures the previous graph doesn't get deleted when you add the
%new one
hold on
%could also plot(months, low, months, high)
plot(months,low,'blue','lineStyle','--')
title ('Months Tempuratures')
xlabel('Months')
ylabel('Temps (F)')
