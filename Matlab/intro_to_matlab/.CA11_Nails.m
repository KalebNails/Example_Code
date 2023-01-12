%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA11
% PROGRAM PURPOSE: to read a file that has grades in it and determines
% how many of them are a's and how many of them are b's...etc and have the
% choice to run it again with a different file
% AUTHOR: Kaleb Nails
% DATE: 3/1/2022

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear, clc

%INPUTS: the excel file name, if they want to continue

%OUTPUTS: how many students are failing or passing etc

%This creates the variables that records how much of each grade their is
Fail = 0;
Dgrade = 0;
Cgrade = 0;
Bgrade = 0;
Agrade = 0;

%This creates the loop variable in order to see if it will continue or quit
%the while loop
loop = 1;
while loop == 1

    %This collects the file name and then passes it to the function to
    %read the file
    filename = input('Enter Filename: ', 's');
    

    %This double checks the user put a valid entry
    while isempty(filename)
        filename = input('Enter Filename: ', 's');
    end

    %Uses a function to read the file
    File = readXLFile(filename);

    %makes a columns of all of the grades, and then runs the for function
    %depending on how long it is
    grades = File(:,2);
    for index = 1:length(grades)
   
        % can also use find() which would be better and easier but this is
        % the requirements
        %To This checks what grade the student got and adds it to the
        %running total of all grade types
        if grades(index,1) < 60 
            %fprintf('you got fail')
            Fail = Fail +1;

        elseif grades(index,1) >= 60 && grades(index,1) < 70
            %fprintf('you got a D')
            Dgrade = Dgrade +1;

        elseif grades(index,1) >= 70 && grades(index,1) < 80
            %fprintf('you got a C')
            Cgrade = Cgrade +1;


        elseif grades(index,1) >= 80 && grades(index,1) < 90
            %fprintf('you got a B')
            Bgrade = Bgrade +1;

        elseif grades(index,1) >= 90 && grades(index,1) < 100
            %fprintf('you got a A')
            Agrade = Agrade +1;
        end
    end

    %Creates a table of all the results
   Table = table(Agrade,Bgrade,Cgrade,Dgrade,Fail,'VariableNames',{'A''s'  'B''s' 'C''s' 'D''s' 'F''s'});
   disp(Table)

   %Checks if they want to continue or if they want to quit, also verifies
   %it is an valid input
   loop = input(['\n would you like to continue \n' ...
        '[1] Yes \n' ...
        '[2] No \n']);

   while loop ~= [1,2]
          loop = input(['\n Invalid entery. Would you like to continue \n' ...
        '[1] Yes \n' ...
        '[2] No \n']);
   end

end







