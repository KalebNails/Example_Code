%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER:HW02 
% PROGRAM PURPOSE: To take data from an excel file and average it then make
% a chart of it
% AUTHOR:Kaleb Nails
% DATE: 1/31/2022
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc, clearvars


%File name i am testing with is stdntData
%This is the user input for the name of the file,the course name and
%semester
filename = input('Please enter the name of the file you are looking for: ','s');
coursename = input('Enter course name: ','s');
Semester = input('Please enter semester: ','s');

%This grabs the matrix from the provided spreadsheet
spreadsheet = readmatrix(filename);

%This gives me the size of the matrix, im looking for the number of columns
[row, column]=size(spreadsheet);

%I use the number of columns to determine the variable lenght of i, this
%means I start i @ 2 because I assume that the first column is the list
%of student numbers
i= 2:column;

%alltest produces a matrix with all the test scores in anysize matrix as
%long as the first column doesnt include test scores. Then take the mean
alltest = spreadsheet(:,i);

% I could use mean(alltest') to get the average test score of each
% individual student but this is just a note to me. Instead ill just
% average all the numbers at once
classavg = mean(alltest,"all");

%Using a double %% puts a % in the text
fprintf('\n The class average of %s %s is %.2f%% \n',coursename, Semester, classavg);

%I then find the average of each test and make a bar graph
testscore = mean(alltest);
bar(testscore);
xlabel('Test number')
ylabel('Grade out of 100')
axis([0 column 0 100])