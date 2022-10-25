%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: Homework 01
% PROGRAM PURPOSE: Calculate the force of drag from 0 to 200 mph on a plane
% AUTHOR: Kaleb Nails
% DATE: 1/12/2022
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc, clearvars
%THEORY: We will be using the drag equation of drag = drag coefficient*density of
%air*Vecolity^square *area/2 to calculate the drag produced on this air
%craft. Drag is the force acted on an object as it moves through a fluid

%OUTPUTS: The force in newtons

%ASSUMPTIONS: The density of air, the drag coefficient, and area is all
%constant throughout the different speeds.

%UNITS: given units are in mph, and output units are in newtons

%we also need to convert from imperial to SI back to imperial units for the
%input velocity.


%This sets up the constants of the simulation
Area = 1;
p=1*10^-6;
Cd = 2.0019*10^7;

%This  creates a matrix of every x needed, and then converts it to m/s and
%squares it
mph= 0:200;
ms = mph./2.37;
vel2 = ms.^2;
%This shows the drag calculation
Drag = p*vel2*Cd*Area*(1/2);
%This grabs every 10th number in the matrixes of speed and drag and
%creates a table with them
nthDrag = Drag(1:10:end)';
nthTable = [mph(1:10:end)', nthDrag];
SpeedvsDrag = array2table(nthTable, 'VariableNames',["Speed (mph)","Drag Force (N)"]);
disp(SpeedvsDrag)
%This displays the plot of the calculated answers
plot(mph, Drag)
xlabel('Speed (mph)')
ylabel('Drag (Nx10^4)')



