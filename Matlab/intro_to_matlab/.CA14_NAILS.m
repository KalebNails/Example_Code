%% In-Class Activity #14
% TOPIC: Basic Image Processing: Changing Color of an Image
% A brief intro to 3D arrays/array referencing practice

% Name: Kaleb Nails
% Date: 3/24/22

% BACKGROUND:Image processing is the generation of a new image from one or more existing images.
% MATLAB makes it easy to work with images by providing some basic functions
% that allow you to read and write images in standard image-file formats, such as JPEG

% Locate the attached photo of a blue bird stored in JPEG format, bbird.jpg (must be on same folder as script). 
% Fill in the ? in the code with correct values to change the color of the
% bird from blue to red.

clear
close all
clc

% Specify URL
img_URL = 'https://images.squarespace-cdn.com/content/v1/56e316c61bbee06d13210ed6/1462558186052-MW2M2EPIDRPO31NLB27G/38368-Mountain-Bluebird.jpg?format=500w';

% Get image from a website
bbird = webread(img_URL);

% Reads the image from a file located in current folder into an array named bbird
%bbird = imread('bbird.jpg'); 

% Displays the image
imshow(bbird)               

% Forces display to have corrected aspect ratio 
axis equal 

% Forces the display to omit “empty” white areas above, below, left, or right of the image.
axis tight                   

% Dimensions of array-note the 3 dimensions
[rows, cols, rgb] = size(bbird);            

% To look at individual values within the array, we need three indices, for example:
%3 columns is the R=1 G=2 B=3, you could also use the colon to grab
%specficic ones
% bbird (236,361,1)
% bbird (236,361,2)
% bbird (236,361,3)

% These three numbers give the values of the red component, the green component,
% and the blue component of the color of the pixel at location 236, 361
% (row 236 from the top, column 361 from the left).
% A pixel is one square piece of a mosaic of colors that make up a digital image, in this
% case a 525-by-775 image, and every pixel consists of three numbers, representing
% the intensities of red, green, and blue light that together create the
% color of the pixel in the human eye. Each of these numbers falls in the range 0
% to 255, with higher values meaning higher intensity

% Suppose we wanted a red bird. We can do a little image processing to
% change the blue bird into a red bird. All it takes is a nested for-loop:

% Copies all the pixels of bbird into rbird.  
rbird = bbird;               

% The nested for-loop allows us to inspect each pixel to see whether it is 
% blue enough to be part of the bluebird’s blue feathers.

tic   % timing the image processing using for-loop

%can also use find to make it faster
for row = 1:rows              
    for col = 1:cols
        
         % The if-statement determines how blue a pixel is. 
         % If the blue channel is more than 20% larger than the mean of the three color channels:
         if bbird(row,col,3) > 1.08 * mean(bbird(row,col,:))
            % it sets the red channel’s value in redbird’s pixel to be equal to the blue channel of bluebird’s pixel
            rbird(row,col,1) = bbird(row,col,3); 
            % It then sets the green and blue channels in redbird’s pixel to zero, so that
            % there is no hint of green or blue
            rbird(row,col,2:3) = 0;
            
        end
    end
end

toc                          % timing the image processing using for-loop

%displays the image
image(rbird) 

%forces diplay to have corrected aspect ratio
axis equal  

%forces the display to omit “empty” white areas above, below, left, or right of the image.
axis tight                   

%display both images side to side 
% by using the brackets, we are creating a new matrix
newBird = [bbird; rbird];
imshow(newBird) 
