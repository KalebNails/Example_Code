%creates a function based on the input file, in 1st and 2nd column
function Table = tableDisp(File)
    heading1 = input('Enter Heading 1: ','s');
    heading2 = input('Enter Heading 2: ','s');
    Table = table(File(:,1),File(:,2),'VariableNames',{heading1  heading2});
    disp(Table)
end
