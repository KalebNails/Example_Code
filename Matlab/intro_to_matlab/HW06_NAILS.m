%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: HMK 6
% PROGRAM PURPOSE:To find error in a read excel file
% AUTHOR: Kaleb Nails
% DATE: 3/24/22
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc, clearvars

%This sets up the while loop and creates text propts.
Continue = 'Y';
Userprompt = 'Enter filename: ';
ErrorMessage = 'Incorrect Entry. Enter filename: ';
Errorcount = 0;

while strcmp(Continue,'Y') == 1
    
    %This asks for the users input for filename and error checks it
    
   filename = input(Userprompt,'s');
   while isempty(filename)
        filename = input(ErrorMessage,'s');
   end
    %This uses a function that reads the fileFile
   File = readXLFile(filename);

   %This determines the size of the file we imported
   [rowsize, columnsize] = size(File);

   %This reads through all of the rows according to the number of rows
   for row = 1:rowsize

       %This checks if the box entry is in the a number, and if it isn't it
       %changes it to zero
       if isnan(File(row,2)) == 1
           File(row,2) = 0;
           Errorcount = Errorcount + 1;
       end
       
   end

   %creates and displays a table of the corrected grades
   Table = table(File(:,1),File(:,2),'VariableNames',{'Students''s'  'Grades''s'});
   disp(Table)
   
   %checks to see if any error checking took place and lets the user know
   %how many
    if Errorcount > 0
        fprintf('There were %d errors in your data \n',Errorcount)

    else
      fprintf('There were no errors in your data \n')  
    end
    %This resets error count in case the user does another run of code
    Errorcount = 0;
    %calls a function to check if the code should continue
    [Continue] = ContinueCode();
    
end

