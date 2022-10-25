%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: HW03
% PROGRAM PURPOSE: To convert Celsius into either fahrenheit and kelvin
% also determine how a machine is opperating at a certain temp
% AUTHOR: Kaleb Nails
% DATE: 2/7/2022
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 clc, clear, clearvars;

%THEORY: in order to convert from C to F you must multiply by 1.8 then add
%32. In order to go from C to K you just add 273.15

%OUTPUTS: The tempurature in F or K. And how well a machine is operationg

%INPUTS: The temp in C, then the temp in F that the machine opperates at

%This collects all the inputs from the uswer
TempC = input('Enter the temp in Degrees C: ');
Unit = input('Do you want F or K? ','s');



%This checks if the unit desired is in F
if 1 == strcmpi(Unit,"F")

    %This calculates temp in F
    TempF = TempC*1.8 +32;
    fprintf('The temp in degrees %s is %.1f \n',Unit,TempF)

    %This calculates temp in K
elseif 1 == strcmpi(Unit,"K")
    TempK = TempC + 273.15;
    fprintf('The temp in degrees %s is %.1f \n',Unit,TempK)

    %This checks for faulty inputs
else
    fprintf('Incorrect input. Only F and K are allowed \n')
end

%% P2
%This asks the user for the temperature of the machine
MachineTemp = input('\n Enter the current temperature of the machine: ');

%This compares the machines temperature to predetermined values and tells
%about the machines current opporating condition
if MachineTemp > 100
    fprintf('Too hot-equipment malfunctioning \n')
    
elseif MachineTemp >=90 && MachineTemp <= 100
    fprintf('Normal operating temperature \n')

elseif MachineTemp >=50 && MachineTemp < 90
    fprintf('Temperature Below Desired Operating Range \n')

elseif MachineTemp < 50
    fprintf('Too Cold - Turn Off Equipment \n')
end




