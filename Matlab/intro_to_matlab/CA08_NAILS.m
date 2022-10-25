%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA08
% PROGRAM PURPOSE: To ask the user what information they want about a data
% set and use functions in order to calculate those
% AUTHORS: Kaleb Nails
% DATE: 2/17/22
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 clc, clear

%INPUT: course, semesterm filenames
%OUTPUT: mean, max, min, plots

course   = input('Enter Course Name: ', 's');
semester = input('Enter Semester: ', 's');
filename = input('Enter Filename: ', 's');

% function readXL here
File = readXLFile(filename);

prompt = sprintf('%s-%s', course, semester);

choice = menu(prompt,... 
'Average Grade','Maximum Grade','Minimum Grade',...
'Final Grades', 'Plot');

%Chooses what function to run based of user input
if choice == 1
    % function meanCalc here
    average = meanCalc(File);
    % display result
    fprintf( '%s grade average is %.1f \n',prompt, average);

elseif choice == 2
    % function maxCalc here
     Maxdatavalue = maxCalc(File);
    % display result
     fprintf( '%s max grade is %.1f \n',prompt, Maxdatavalue);

elseif choice == 3
    % function minCalc here
    Mindatavalue = minCalc(File);
    % display result
    fprintf( '%s min grade is %.1f \n',prompt, Mindatavalue);

elseif choice == 4
    % function tableDisp here
       Table = tableDisp(File);

elseif choice == 5
    % function plotXY here
    mygraph = plotXY(File);
end