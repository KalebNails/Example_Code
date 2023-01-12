%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA09
% PROGRAM PURPOSE: To have a player set a range then another player guess a
% random number within that range, must use while and functions
% AUTHOR:Kaleb Nails
% DATE: 2/22/22
% CREDIT TO(if applicable):

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc, clear
fprintf('Welcome to the guessing game!  \n');

%Collect the users username
Username = input('Please enter your name: ','s');
Difficultly = input(['Pick a difficultly (1,3,5)\n' ...
    '[1] Hard (1 guess) \n' ...
    '[3] Medium (3 guesses) \n' ...
    '[5] Easy (5 guesses) \n']);  

%This checks that the difficultly is a valid number
while Difficultly ~= [1,3,5]

    fprintf('please select a valid game mode.\n')
    Difficultly = input(['Pick a difficultly (1-3)\n' ...
    '[1] Hard' ...
    '[2] Medium' ...
    '[3] Easy']);  
end
clc

%This uses the randnum function
[Upperlimit , Lowerlimit, Random_number] =  randNum();

%ask the 2nd player for their name
twoplayer = input('Please enter your name: ','s');

clc

%inquires the second users input
prompt = sprintf('\n Please guess a whole number from %d to %d: ', Lowerlimit,Upperlimit);
Userguess = input(prompt);

%This checks if the user guessed the original number correctly then it
%checks that its within the range of the limits provided by the function.
while Userguess ~= Random_number && Difficultly ~= 1 || isempty(Userguess)

    while Userguess > Upperlimit || Userguess < Lowerlimit
        clc
        fprintf('number out of range');
        Userguess = input(prompt);
        
    end
    clc
    %This counts the number of guesses depending on the difficultly and
    %lets the user guess again
    if Userguess ~= Random_number
         Difficultly = Difficultly - 1;
         fprintf('wrong number try again \n you have %d remaining',Difficultly);
         Userguess = input(prompt);
    end

end

%After it continues it tells you you got it right but checks that you didnt
%use all of your guesses
if Difficultly ~= 1
    fprintf('congrats! you got the number! It is %d \n',Random_number)
else
    fprintf('too bad try again next time \n')
end

