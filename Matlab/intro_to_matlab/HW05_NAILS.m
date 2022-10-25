 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: HW05
% PROGRAM PURPOSE:To use function to convert from F to C and vise versa and
% error check the users input, but also ask if they want to want to run the
% program again
% AUTHOR: Kaleb Nails
% DATE: 2/22/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %clear

%INPUT: which function it wants to run, and the temp
%OOUTPUT: Temp in the correct unit
iterate = 1; 
endcount = 0;

while  iterate == 1

   %This asks the user whether they want to go from c2f or f2c
    Prgramtype = input(['Which would you like to run:\n' ...
    'Celsius-to-Fahrenheit [1]\n' ...
    'Fahrenheit to Celsius [2]\n' ...
    'Or [3] to quit \n']);

    %This checks that the user inputs a valid answer
    while Prgramtype ~= [1,2,3]
        fprintf('please enter a valid number (1 or 2) \n')
        Prgramtype = input(['Which would you like to run:\n' ...
            'Celsius-to-Fahrenheit [1]\n' ...
            'Fahrenheit to Celsius [2]\n']);
    end
    
    %This sees which one it choose and calls the appropriate function which
    %converts the temp, then this script prints the results
    if Prgramtype == 1
        Celsius = input('Enter a temp value (C): ');
        temp  = c2f(Celsius);
        fprintf('The value you entered, %.1f in C, is equal to %.1f in F. \n', Celsius, temp);
    
    elseif Prgramtype == 2
        Fahrenheit = input('Enter a temp value (F): ');
        temp = f2c(Fahrenheit);
        fprintf('The value you entered, %.1f in F, is equal to %.1f in C. \n', Fahrenheit, temp);

    elseif Prgramtype == 3
        fprintf('Have a Nice Day! \n');
        iterate = 2;
    end

    while (iterate == 1 && endcount == 0) %| iterate ~= [1,2]
       iterate = input(['\n would you like to continue \n' ...
           '[1] Yes \n' ...
           '[2] No \n']);
       endcount = 1;
    end
        endcount =0;
end