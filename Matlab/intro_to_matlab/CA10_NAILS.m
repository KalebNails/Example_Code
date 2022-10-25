%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ASSIGNMENT TYPE AND NUMBER: CA10
% PROGRAM PURPOSE: Create a random number guessing game where it tells the
% user if it was too far above/below or spot on
% AUTHOR:Kaleb Nails
% DATE: 2/23/2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear, %clc
%INPUT: upper and lower limit of the random number generation, the users
%name, the users guess

%OUTPUTS: whether the user is too high, too low, or if they guessed the
%correct number

fprintf('Welcome to the guessing game!  \n');

%Collect the users username and sets the number of guesses
Username = input('Please enter your name: ','s');
Difficultly = 5;

%This uses the user defined randnum function
[Upperlimit , Lowerlimit, Random_number] =  randNum();

%clc

%inquires the guess of the user
prompt = sprintf('\n Please guess a whole number from %d to %d: ', Lowerlimit,Upperlimit);
Userguess = input(prompt);

%This checks if the user guessed the original number correctly then it
%checks that its within the range of the limits provided by the function.
while Userguess ~= Random_number && Difficultly ~= 1 || isempty(Userguess)

    while Userguess > Upperlimit || Userguess < Lowerlimit
        %clc
        fprintf('number out of range');
        Userguess = input(prompt);
        
    end
    %clc
    %This counts the number of guesses depending on the difficultly and
    %lets the user guess again, checks if the guess is the random number
    %and whether it is too high or too low
    if Userguess ~= Random_number && Userguess < Random_number
         Difficultly = Difficultly - 1;
         fprintf('Your number is too Low! \n you have %d remaining %s',Difficultly, Username);
         Userguess = input(prompt);

    elseif Userguess > Random_number && Userguess ~= Random_number
         Difficultly = Difficultly - 1;
         fprintf('Your number is too High! \n you have %d remaining %s',Difficultly,Username);
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



