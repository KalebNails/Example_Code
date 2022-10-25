%ask for interval of the number, then produce a random number betwee those
%two numbers and return them. checks that the inputs are valid
function [Upperlimit , Lowerlimit, Random_number] =  randNum()

    %Asks for the upperlimit from the user
    
    Upperlimit = input('What is the upper limit for your guess: ');

    %checks to make sure that it is not an empty entry and has a variable
    %entered
    while isempty(Upperlimit) || round(Upperlimit) ~= Upperlimit || Upperlimit < 0
           Upperlimit =input('upper limit cannot be empty or non integer number. \n What is the upper limit for your guess: ');
    end

    %This asks and checks about the lower limit of the number
    Lowerlimit = input('What is the lower limit: ');
    while isempty(Lowerlimit)  || round(Lowerlimit) ~= Lowerlimit || Lowerlimit < 0
           Lowerlimit =input('Lowerlimit cannot be empty or a non integer number. \n What is the upper limit for your guess: ');

    end
    %This produces the random number based on the lower and upper bounds
    %Random_number = rand(1,1)*(Upperlimit-Lowerlimit)+Lowerlimit;
    Random_number = randi([Lowerlimit,Upperlimit]);