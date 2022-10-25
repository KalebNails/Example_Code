%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: HMK_07
% PROGRAM PURPOSE: To find average rain data and display a graph to the
% user from a large data set
% AUTHOR: Kaleb Nails
% DATE: 04/6/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%I COULD have just used this datetime(dates).Month()  but im stupid and
%didnt know it until after I did it

close, clear, clearvars, clc

%this sets up the loop of the code
Continue = 'Y';
while strcmp(Continue, 'Y') == 1
    close
    
    %This function asks the user for the file that needs to be read
    [File] = readXL();

    %This defines what month the user wants to find.
    Userprompt = 'What month would you like to analyse [1-12] \n';
    ErrorMessage = 'Invalid input. What month would you like to analyse [1-12] \n';

    %This function error checks, but it can be any positive number, so we
    %limit it by adding another condition below.
    [Response] = usernumberinput(Userprompt,ErrorMessage);
    while Response > 12
        fprintf('That number is too high. ')
        [Response] = usernumberinput(Userprompt,ErrorMessage);
    end

    MonthDesired = Response;
    %This removes the titles from the spreadsheet
    File(1,:) =[];
    Dates = File(:,3);
    AvgWind = File(:,4);
    AvgPrecip = File(:,5);
    AvgTemp = File(:,6);
    HighTemp = File(:,7);
    LowTemp = File(:,8);

    %This splits up the data types in the file

    %This identifies the dates used and selects ten first 2 lines of code
    Dates = cell2mat(Dates);
    Months = char(Dates);
    Days = Months(:,4:5);
    Days = str2num(Days(:,1:2));
    Months = Months(:,1:2);
    Months = str2num(Months(:,1:2));
    [Monthslocations, ~, ~]  = find( Months ==  MonthDesired);

    %Now we calculate the total number of inches of rain
    AvgPrecip = cell2mat(AvgPrecip);
    Raincount = sum(AvgPrecip(Monthslocations));

    %Now we calculate avg wind speed
   AvgWind = cell2mat(AvgWind);
   TrueAvgWind = mean(AvgWind(Monthslocations));

   %This is to plot the TEMPS
   AvgTemp = cell2mat(AvgTemp);
   HighTemp = cell2mat(HighTemp);
   LowTemp = cell2mat(LowTemp);
   PreviewDay = Days(Monthslocations); 
   PreviewAvgTemp = AvgTemp(Monthslocations);
   PreviewHighTemp = HighTemp(Monthslocations);
   PreviewLowTemp = LowTemp(Monthslocations);

    %This creates the name of the graphs
   titlecard = sprintf('The temperature for Month %d in 2017 in Daytona',MonthDesired);

   %This is to plot the F graph
   subplot(2,1,1)
   plot(PreviewDay, PreviewAvgTemp)
   hold on 
   plot(PreviewDay, PreviewLowTemp)
   hold on
   plot(PreviewDay, PreviewHighTemp)
   title(titlecard)
   xlabel('Days')
   ylabel('Temps in F')

   %This converts to celsius for all of them
   Fahrenheit = PreviewAvgTemp;
   temp=f2c(Fahrenheit);
   PreviewAvgTempC = temp;

   Fahrenheit = PreviewLowTemp;
   temp=f2c(Fahrenheit);
   PreviewLowTempC = temp;

   Fahrenheit = PreviewHighTemp;
   temp=f2c(Fahrenheit);
   PreviewHighTempC = temp;
    
   %This is used to plot all of the data
   subplot(2,1,2)
   plot(PreviewDay, PreviewAvgTempC)
   hold on 
   plot(PreviewDay, PreviewLowTempC)
   hold on
   plot(PreviewDay, PreviewHighTempC)

   title(titlecard)
   xlabel('Days')
   ylabel('Temps in C')

fprintf('Month %d it rained %.2f inches \n', MonthDesired, Raincount)
fprintf('The average wind speed was %.2f \n' , TrueAvgWind)

    %This function checks if the code wants to continue
    [Continue] = ContinueCode();
end

