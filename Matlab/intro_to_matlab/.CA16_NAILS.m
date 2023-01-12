%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA16
% PROGRAM PURPOSE: to pull data from a spread sheet about racers and be
% able to display data about them
% AUTHOR: Kaleb Nails
% DATE:4/1/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc, clear, clearvars, close

%OUTPUT: first place winner and time, as well as where they live
%last place time and where they live
%female to male ratio
%age of the youngest and oldest runner

% Enter your state and tell how many runners from your state
[File] = readXL();

%This breaks up the excel sheet into its components
Names = cellstr(File(:,4));
County = cellstr(File(:,7));
State = cellstr(File(:,8));
Gender = cellstr(File(:,6));

%Find the min and max runner
TotalTime = File(:,11);
TotalTime = cell2mat(TotalTime);
[rowmax, wheremax] = max(TotalTime);
[rowmin, wheremin] = min(TotalTime);

%display name and time of racer
slowest = datetime(rowmax,'ConvertFrom','datenum');
slowest.Format = 'HH:mm:ss';
Winner = cell2mat(Names(wheremax,1));
fprintf("the runner with the most time is %s with a time of %s \n",Winner,slowest);

%This determines where the winner / loser is from
CountyWinner = cell2mat(County(wheremax,1));
StateWinner = cell2mat(State(wheremax,1));
fprintf("%s is from %s, %s \n", Winner, CountyWinner, StateWinner)

%displays the the fastest time or the runners and the slowest
fastest = datetime(rowmin,'ConvertFrom','datenum');
fastest.Format = 'HH:mm:ss';
loser = cell2mat(Names(wheremin,1));
fprintf("the runner with the least time is %s with a time of %s \n",loser,fastest);
Countyloser = cell2mat(County(wheremin,1));
Stateloser = cell2mat(State(wheremin,1));
fprintf("%s is from %s, %s \n", loser, Countyloser, Stateloser)

%This finds gender, it finds the number of M's then converts it into a
%matrix then counts the number of appearences
Gender =cellstr(Gender);
Nummales = length(cell2mat(strfind(Gender,'M')));
Numfemales = length(cell2mat(strfind(Gender,'F')));

fprintf('The number of female runners is: %d \n and the number of male runners is: %d \n',Numfemales,Nummales);

%This pulls the age of the users
Age = cell2mat(File(:,5));
MaxAge = max(Age);
MinAge = min(Age);
fprintf('The youngling of the group is %d years old. \n', MinAge)
fprintf('The geriatric is %d years old \n',MaxAge)

%This asks the user what state they are from and sets variables to define
%it, also error checks it
LocationQ = 'What state are you from [ST]: ';
Homeland = input(LocationQ, 's');

while isempty(Homeland) | 1 ~= ismember(Homeland,State) 
    Homeland = input('invalid input %s',LocationQ, 's');
end

%This counts creates a matrix that contains if the statement is true or
%false. This is a ery abou
Sharedlocals = count(State,Homeland);

%This counts the number of people from your state.
Sharedlocalcounts = length(nonzeros(Sharedlocals));
fprintf('There are %d runners from %s \n',Sharedlocalcounts, Homeland);

%this creates the pie chart
PieData = [Nummales, Numfemales];
labels = {'Males','Females'};
pie(PieData)

%This is used to create a legend and a title, title must be below pie chart
title('Male vs. Female Runners')
legend(labels,'Location','southoutside','Orientation','horizontal')


