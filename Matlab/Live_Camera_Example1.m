%Kaleb Nails
%Created: 2/~/2022
%modified: 10/25/2022
%purpose: To create a live camera feed in a simple manor


clear, clc,close;
load('cameraParams.mat')
cam = webcam('Integrated Webcam');

img = snapshot(cam);
Undistorted = undistortImage(img, cameraParams);
[rowsize, columnsize,Deep] = size(Undistorted);
pause(.5)

for timer = 1:150
rowlocations = 0;
columnlocations = 0;
img = snapshot(cam);
Undistorted = undistortImage(img, cameraParams);


locations = Undistorted(:,:,2);
meancolor = Undistorted(:,:,1) + Undistorted(:,:,2) + Undistorted(:,:,3);
meancolor = meancolor/3;
meancolor = 2.7*meancolor;


[rowlocations, columnlocations] = find(locations > meancolor);
Specailcolorlocation = [rowlocations; columnlocations];


axis equal
axis tight
imshow(Undistorted);
hold on
pause(.002)
end
