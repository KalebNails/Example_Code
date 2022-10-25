%This calculates the mean of a given data set, in the second column
function average = meanCalc(File)
    average = sum(File(:,2))/numel(File(:,2));
end
    