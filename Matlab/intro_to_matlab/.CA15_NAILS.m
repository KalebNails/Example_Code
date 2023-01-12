%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA15
% PROGRAM PURPOSE: To find cars with a certian fuel efficiency.
% AUTHOR: Kaleb Nails
% DATE: 3/29/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Find car models with 30mpg+ fuel efficiency

clc
clear
Continue = 'Y';

%This repeats the whole code and the process
while strcmp(Continue,'Y') ==1

    %This function error checks and returns a cell type of file
    [File] = readXL();
    carData = File;
    
    % Get mpg's from carData
    mpgCell = carData(:,2);
    
    % Removes title, can do this here because it is a (:,1) length matrix
    % so it its still rectangular
    mpgCell(1) = [];

    % Converts from cell to numeric type
    mpg = cell2mat(mpgCell);
    
    % Get model from carData, this selects it all except the first one
    % where that is just title not being selected
    model = carData(2:end,1);
     
    % Looking for mpg >= 30 
    for row = 1:length(mpg)

        %This works be recording the row as it goes along and after
        %removing all the zeros from the locations
        if mpg(row) >= 30
           idxmpg(row) = row;
        end
    end
        
   %This gets rid of the nonzero cells, because it is recording the
   %number of the row, where that number of the row occurs, so it has
   %gaps of zeros that need to be removed
    idxmpg = nonzeros(idxmpg);
    mpg30 = mpg(idxmpg);
    model30 = model(idxmpg);

    % Converts to cell type, and creates a table of wanted variables
    mpg30 = num2cell(mpg30);
    XLtable = [{'MODEL', 'MPG'}; model30, mpg30];
   
    
    % Creates MS Excel file mpgXL.xlsx 
    writecell(XLtable,'mpgXL.xlsx' )

    %This function checks if the user wants to repeat this whole process
    [Continue] = ContinueCode();
end

