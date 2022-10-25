%This function creates a random matrix that generates numbers between 0 and
%1 that the user gets to decide the size of

function [RndMatrix] = ReadMatrix()
    
    %This checks variables and doesnt return an error if you input text,
    %instead it takes it as a string, then converts it to a decimal or a
    %NaN and then the while loop checks if the NaN was produced. This error
    %checks the input.
    Columnsize = input('Enter Number of columns: ','s');
    Columnsize = str2double(Columnsize);

    while isnan(Columnsize)| isempty(Columnsize) | Columnsize <= 0 | Columnsize / round(Columnsize) ~= 1
        Columnsize = input('Incorrect Entry. Enter Number of columns: ','s');
        Columnsize = str2double(Columnsize);
    end

    Rowsize = input('Enter Number of rows: ','s');
    Rowsize = str2double(Rowsize);

    while isnan(Rowsize) | isempty(Rowsize) | Rowsize <= 0 | Rowsize / round(Rowsize) ~= 1
        Rowsize = input('Incorrect Entry. Enter Number of rows: ','s');
        Rowsize = str2double(Rowsize);
    end   

    RndMatrix = rand(Rowsize,Columnsize);

end