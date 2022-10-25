
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA06
% PROGRAM PURPOSE: To find the area and volume of a given shape with given
% dimesions
% AUTHOR:Kaleb Nails
% DATE:2/3/2022
% CREDIT TO(if applicable): EGR 115 Class

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear, 

% User selection of shape
Shape = input(sprintf('Enter shape of area:\n 1 = circle\n 2 = square\n 3 = rectangle\n 4 = triangle\n 5 = other\n> ' ));

if Shape == 1
    % Input and calculation for area and volume of circle
    Diameter = input('What is the diameter of your circle? ');
    Area = pi * (Diameter/2)^2; 
    Volume = (4/3)*pi * (Diameter/2)^3;

elseif Shape == 2
    % Input and calculation for area and volume of square
    Side = input('What is the length of one of the sides of your square? ');
    Area = Side^2;
    Volume = Side^3;

elseif Shape == 3
    % Inputs and calculation for area of rectangle
    Length = input('What is the length of your rectangle? ');
    Width  = input('What is the width of your rectangle? ');
    Area   = Length * Width;

elseif Shape == 4
    % Inputs and calculation for area of triangle
    Base   = input('What is the base of your triangle? ');
    Height = input('What is the height of your triangle? ');
    Area   = (1/2) * Base * Height;

    %Catches wrong or outling answers
elseif Shape == 5
    fprintf('I am sorry this program cannot calculate the area of your shape. \n')

else
    fprintf('Invalid Input. Please only enter a number between 1-5. \n Shutting Program Down Now..... \n')
end

%If the original input was right it runs the code below, if not the program
%just ends
if Shape <=4 && Shape >=1

    % User input of the units that will be used for the area
    Units = input('What are the units you will use to calculate the area of your shape? ', 's'); % This input will take in text. 
    
    % Output the area of the shape that was calculated for circle, square,
    % rectange, or triangle (%s will display the text that the user put for the
    % units input: Units = input('What are the units you you will use to calculate the area of your shape? ', 's') 
    fprintf('The area of your shape is %.2f %s squared \n ', Area, Units)

    %This checks if the users want to continue and calculate volume
    Continue = input('Would you like to find the volume of the cross-section of your shape?[Y/N]:','s');

    %Checks if the user says yes, or checks if the user says no, if no it
    %shuts the program down
    if strcmp('Y', Continue) == 1 

        %These shapes did not need more information so the volume was
        %calculated earlier, it is displayed here
        if Shape == 1 || Shape == 2
            fprintf('The volume of your shape is %.2f %s cubed \n',Volume, Units)

         %There shapes need aditional information in order to calculate the
         %volume, below it asks and then caclulates the volume
        elseif Shape == 3 || Shape == 4
            width = input('Please select the height of the shape: ');
            Volume = Area*width;
            fprintf('The volume of your shape is %.2f %s cubed \n',Volume, Units)
            
        %This is a catchall for all the wrong answers
        else
        fprintf('Invalid input, please try again. \n')
        end
    else
        fprintf('Shutting Program Down Now.....')
    end
end
