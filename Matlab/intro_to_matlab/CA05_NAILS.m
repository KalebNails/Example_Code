
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA05
% PROGRAM PURPOSE: To take in the usersname and have them guess a number
% then tell them if it is the correct number or if it is to high, or too
% low
% AUTHOR: Kaleb Nails
% DATE: 2/1/22
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc, clear, clearvars
%INPUTS: The Users name and his/hers guess to what the random number is
%OUTPUT: if the guess was over or under or spot on

fprintf('Welcome to the RNG ring, get ready to guess a number from 1 to 10! \n');

%now we will produce the random interger between Upperbound and Lowerbound
%which could be modified to have the user decided if needed
Upperbound = 10;
Lowerbound = 1;
rndnumber = randi([Lowerbound,Upperbound],1);

%Below we will collect our inputs 
name = input('Please enter your name: ','s');
guess = input('Please enter your guess: ');

%Now we will check if they guessed the number and futher down we use elseif
%and the AND comparison to check if the number is within the range of
%Upperbound and Lowerbound
if guess == rndnumber
    fprintf('You Guessed The Number %s! \n',name);

elseif (Upperbound>= guess) && (guess > rndnumber)
    fprintf(['Sorry you guess was TOO high %s! \n' ...
        ' The number was %d! \n'],name,rndnumber);

elseif (Lowerbound <= guess) && (guess < rndnumber)
    fprintf(['Sorry you guess was TOO low %s! \n' ...
        ' The number was %d! \n'],name,rndnumber);

else
    clc
    fprintf(['Pick a number from [1, 10] next time. %d is outside of the range "%s"! ' ...
        '\n If that even is your real name. \n'],guess,name)
end

