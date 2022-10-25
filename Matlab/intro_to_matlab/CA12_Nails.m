%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: In-Class Activity #12
% PROGRAM PURPOSE: to simulate a persons daily nutrition
% AUTHOR: Kaleb Nails
% DATE: 3/3/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%{
Simulate a person's daily nutritional information for a period of two
weeks (1-14 days).
Data to generate: 
carbs:     [225-325]
proteins:    [45-65]
fats:        [50-70]
calories:[1800-2000]


plot all four datasets into the same figure (but not on the same graph)
Add a baseline to each graph. Have user enter this value. 
%}

%clear,clc, clearvars, 
close
fprintf('************************************')
fprintf('\nNUTRITIONAL INFORMATION SIMULATOR\n')
fprintf('************************************\n')
% Define datasets for nutritional information

carbs = rand(14,1)*(325-225)+225;
proteins = rand(14,1)*(65-45)+45;
fats = rand(14,1)*(70-50)+50;
calories = rand(14,1)*(2000-1800)+1800;



% Request baseline value information from user for each dataset

idealcarbs = input('Input your idea carb intake [from 225 to 325]: ');
idealprotein = input('Input your idea protein intake [from 45 to 65]: ');
idealfat = input('Input your idea fat intake [from 50 to 70]: ');
idealcalories = input('Input your idea calories intake [from 1800 to 2000]: ');

% carbs
subplot(2,2,1)
plot(linspace(0,14,500),idealcarbs,'r*','MarkerSize',1)
hold on
plot(1:14,carbs, '-b', 'LineWidth', 1)
axis ([0 14 200 350])
xlabel('Days')
ylabel ('Daily intake (grams)')
title('Carbs')

% protein
subplot(2,2,2)
plot(linspace(0,14,500),idealprotein,'r*','MarkerSize',1)
hold on
plot(1:14,proteins, '-b', 'LineWidth', 1)
axis ([0 14 45 65])
xlabel ('Days')
ylabel ('Daily intake (grams)')
title('protien')

% fats
subplot(2,2,3)
plot(linspace(0,14,500),idealfat,'r*','MarkerSize',1)
hold on
plot(1:14,fats, '-b', 'LineWidth', 1)
axis ([0 14 50 70])
xlabel ('Days')
ylabel ('Daily intake (grams)')
title('fats')

% calories
% fats
subplot(2,2,4)
plot(linspace(0,14,500),idealcalories,'r*','MarkerSize',1)
hold on
plot(1:14,calories, '-b', 'LineWidth', 1)
axis ([0 14 1800 2000])
xlabel ('Days')
ylabel ('Daily intake (grams)')
title('calories')

% USER CHOICE: To display calorie average
%creaes a variable that runs the while loop
calculatecalories = input(['Would you like to continue? \n' ...
    'Yes [1] \n' ...
    'No [2] ']);
while isempty(calculatecalories) | calculatecalories ~= [1,2]
calculatecalories = input(['Would you like to calculate average calories? \n' ...
    'Yes [1] \n' ...
    'No [2] ']);
end

if calculatecalories == 1
    averagecalories = mean(calories); 
    fprintf('you average %.1f in a time period of 2 weeks \n' , averagecalories)
else
    fprintf('you chose to exit the program \n')
end
