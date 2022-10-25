%Kaleb Nails


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

%compare = [img,Undistorted];

%imshow(compare)

locations = Undistorted(:,:,2);
meancolor = Undistorted(:,:,1) + Undistorted(:,:,2) + Undistorted(:,:,3);
meancolor = meancolor/3;
meancolor = 2.7*meancolor;


[rowlocations, columnlocations] = find(locations > meancolor);
Specailcolorlocation = [rowlocations; columnlocations];

%plot(rowlocation,collocation,'b*','MarkerSize',2);
hold on

%{
tic
for row = 1:rowsize              
    for col = 1:columnsize
        

         if Undistorted(row,col,1) > 1.8 * mean(Undistorted(row,col,:)) 
                        Undistorted(row,col,3) = Undistorted(row,col,1); 
            % It then sets the green and blue channels in redbird’s pixel to zero, so that
            % there is no hint of green or blue
            Undistorted(row,col,1:2) = 0; 


            
        end
    end
end

toc       
%}

axis equal
axis tight
imshow(Undistorted);
hold on
%tic
%{
for r = 1:1800:length(columnlocations)
plot(columnlocations(r,1),rowlocations(r,1),'b*','MarkerSize',4);
hold on
%toc
end
%}
pause(.002)
end
%Undistorted(rowlocations,columnlocations,1:3)