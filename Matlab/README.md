# Why is this empty #
A large amount of my matlab code is either for a class or for a project. So posting it online is not great. Thus a lot of my matlab code is just private. Most of the other matlab code is in seperate repositories. 

# MATLAB Files #


## Parabolic intercept ##
This is software that takes an imaginary ball at the center at some point, calculates it maximium envelope or furthest point it can physically reach based on gravity, and initial speeds.
Then it can calculate another parabolas interception point. This is shown in the image below. At some point i want to consider launch times, and other parameters. I would also at some point like
incorperate drag into the envelope calculations.

![image](https://github.com/KalebNails/Matlab_Balistics_Interception/assets/102830532/262079f7-5b27-4077-aa93-40cce7fc3f0f)



 ## Lab_1_Code_Modified.mlx ##
 ### Overview ###
This MATLAB Live Script (.mlx) file processes experimental data to calculate airspeed, uncertainties, and Reynolds number. The script then generates a plot of airspeed vs. frequency and creates a table with Reynolds numbers for each set of experimental conditions.

### Usage ###
Open Lab_1_Code_Modified.mlx in MATLAB.
Make sure the required data files (Dp_data_1.mat, Dp_data_2.mat, etc.) are in the same directory.
Run the script to perform calculations and generate the desired outputs.

### Contents ####
* Data loading and preprocessing
* Calculation of mean airspeeds and uncertainties
* Plotting airspeed vs. frequency with error bars
* Calculation and display of Reynolds numbers
* Interpolation function for frequency based on airspeed

## Live_Camera_Example1.m ##
### Overview ### 
This MATLAB script (Live_Camera_Example1.m) captures a live camera feed, processes the image, and identifies regions with specific colors. It uses the undistorted image based on camera calibration parameters.

### Usage ###
Open Live_Camera_Example1.m in MATLAB.
Make sure the required cameraParams.mat file is in the same directory.
Connect a webcam to your system.
Run the script to start the live camera feed and color-based region identification.

### Contents ####
* Initialization and loading of camera parameters
* Live camera feed capture and undistortion
* Identification of regions with specific colors
* structs_stress_shear.m

### Overview ### 
This MATLAB script (structs_stress_shear.m) calculates the centroid, moment of inertia, and shear and normal stresses for a set of points with associated areas. It then outputs the results and generates shear and normal stress equations.

### Usage ###
Open structs_stress_shear.m in MATLAB.
Run the script to calculate centroid, moment of inertia, and stresses for the provided points.

### Contents ####
* Calculation of centroid coordinates and shifting points to centroid's reference frame
* Calculation of moment of inertia and shear and normal stresses
* Display of results and stress equations
