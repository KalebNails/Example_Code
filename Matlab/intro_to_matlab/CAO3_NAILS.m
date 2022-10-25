%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: Homework 01
% PROGRAM PURPOSE: Estimate the number of rabbits overtime according to
% initial values, and show on a graph
% AUTHOR: Kaleb Nails
% DATE: 1/12/2022
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc, clear
%OUTPUTS: Estimated number of rabbits according to the initail number of
%values and years, and graph

%THOERY: The math used should create an exponential function, which 
%has the range of  all real numbers and constantly approaches the x axis
%but never reaches it. This graph model the exponetial growth of the
%rabbits as more rabbits lead to more rabbit babbies.

%ASSUMPTIONS: An average pair of rabbit produces 7 babbies in a year. 
%There is not a limiting factor in rabbit population

%UNITS: Years, and rabbits

%get data from user
P0 = input('Enter the intial rabit population (min 2): ');
t = input('Enter the number of years (whole numbers): ');

%Plug inputs into equations
years= 0:0.25:t;

P = P0*(3.5.^years);
%Format bank turns all matrices into whole numbers
format bank

%This converts what we calculated into columns then plots them in a graph
Ptable = [ years',P'];
plot(Ptable(:,1),Ptable(:,2));

%This makes the range of the graph from 0 to the max x and y so it fits
axis([0 years(end) 0 P(end) ])
xlabel ('Years')
ylabel ('Rabbits')

%change round p and t to be the last element of the matrix using numel() to
%get the last one
Table = array2table(Ptable,'VariableNames',["Years","Rabbits"])
fprintf('The rabbit population is estimated to be %.1f in %d years. \n', round(P(end)),t)
