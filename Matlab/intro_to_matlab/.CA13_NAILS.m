%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA13
% PROGRAM PURPOSE:Create a randomly generate matrix of numbers between 0
% and 1 and then round them to either zero or one
% AUTHOR: Kaleb Nails
% DATE: 3/22/22
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc, clearvars


%create a while loop that repeats the whole function
Continue = 'Y';

while strcmp(Continue, 'Y') == 1
    %call the function that creates a user chosen sized matrix filled with
    %random numbers
    [RndMatrix] = ReadMatrix();
    
    %This determines the size of the matrix
    [Num_rows, Num_columns] = size(RndMatrix);
    
    %This creates an empty matrix full of zeros to be filled with the rounded
    %values
    AugmentMatrix = zeros(Num_rows,Num_columns);
    
    %This uses 2 nested for loops to go across the matrix from left to right
    %then top to bottom
    for Column = 1:Num_columns
        
        for Row = 1:Num_rows
    
            %Check if the variable is less the .5 if it is it sets it equal to
            %zero
            if RndMatrix(Row, Column) < .5
                AugmentMatrix(Row, Column) = 0;
    
            %Because of how the random function works there is no need to use
            %any other booleans to check. The number will be bounded by (0,1).
            %Therefore I only need to use an else.
            else
             AugmentMatrix(Row, Column) = 1; 
             
            end
        end
    end
    
    %This displays the old and new matrix on the command window
    fprintf('Old Matrix: \n');
    disp(RndMatrix);
    fprintf('New Matrix: \n');
    disp(AugmentMatrix);
    
    %This checks if the user wants to continue by comparing strings
    check = {'Y','N'};
    Continue = input('Would you like to enter another file? [Y/N]: ','s');
    
    %This error checks the users input
    while isempty(Continue) | strcmp(Continue,check) == 0
        Continue = input('Invalid Input. Would you like to enter another file? [Y/N]: ','s');

    end        
end
fprintf('Have a nice day. \n')

