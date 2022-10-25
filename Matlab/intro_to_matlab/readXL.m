%Reads a file and returns a cell type
function [File] = readXL()

    %collects the name of the file and checks for user error input
    filename = input('Please enter your filename: ','s');
    %This is to let the user not worry about typing .xlsx in order to read
    %the file
    filename = strcat(filename, '.xlsx');
    while isempty(filename) |  0 == isfile(filename)
        filename = input('Invalid input. Please enter your filename: ','s');
        filename = strcat(filename, '.xlsx');
    end
    File = readcell(filename);


end
