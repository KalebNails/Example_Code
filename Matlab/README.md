# Why is this empty

  
A large amount of my MATLAB code is either for a class or for a project. So posting it online is not ideal. Therefore, a lot of my MATLAB code remains private. Most of the other MATLAB code resides in separate repositories.



---

# MATLAB Files

<details>
  <summary><strong>threeD_two_parabolas_collide.m</strong></summary>
  
This software calculates the maximum envelope (furthest reachable point) for a projectile under gravity and initial speeds, then determines how another parabola (a second projectile) can intercept that trajectory. Future improvements may include launching time offsets, additional parameters, and drag considerations.

![image](https://github.com/KalebNails/Matlab_Balistics_Interception/assets/102830532/262079f7-5b27-4077-aa93-40cce7fc3f0f)

</details>

<details>
  <summary><strong>Space Mech Project 1 Code</strong></summary>
  
This MATLAB script demonstrates various orbital mechanics calculations, focusing on determining orbital elements (e.g., semi-major axis, eccentricity, inclination) from position and velocity vectors. It identifies the orbital regime—circular, elliptical, parabolic, or hyperbolic—based on eccentricity, plots effective potential curves, performs numerical integration (ODE45) for two-body motion, and calculates time-based changes in true anomaly. Helper functions compute angular momentum, specific orbital energy, and transformations between orbital element space and Cartesian coordinates.

![image](https://github.com/user-attachments/assets/a20c091c-43d0-4b6d-a18c-238b12146771)
![image](https://github.com/user-attachments/assets/9e118b17-261f-44bd-8b92-97c5713dff4c)


</details>

<details>
  <summary><strong>Lab_1_Code_Modified.mlx</strong></summary>
  
### Overview
This MATLAB Live Script (.mlx) processes experimental data to calculate airspeed, uncertainties, and Reynolds numbers. It then generates a plot of airspeed vs. frequency and creates a table with Reynolds numbers for each set of conditions.

### Usage
1. Open `Lab_1_Code_Modified.mlx` in MATLAB.  
2. Ensure required data files (e.g., `Dp_data_1.mat`, `Dp_data_2.mat`) are in the same directory.  
3. Run the script to perform calculations and produce outputs.

### Contents
* Data loading and preprocessing  
* Calculation of mean airspeeds and uncertainties  
* Plotting airspeed vs. frequency with error bars  
* Calculation and display of Reynolds numbers  
* Interpolation function for frequency based on airspeed

</details>

<details>
  <summary><strong>Live_Camera_Example1.m</strong></summary>
  
### Overview
This MATLAB script captures a live camera feed, processes the image, and identifies regions of specific colors. It uses undistorted images based on camera calibration parameters.

### Usage
1. Open `Live_Camera_Example1.m` in MATLAB.  
2. Ensure the `cameraParams.mat` file is in the same directory.  
3. Connect a webcam.  
4. Run the script to start the live feed and color-based region detection.

### Contents
* Initialization and loading of camera parameters  
* Live camera feed capture and undistortion  
* Identification of regions with specific colors

</details>

<details>
  <summary><strong>structs_stress_shear.m</strong></summary>
  
### Overview
Calculates the centroid, moment of inertia, and shear/normal stresses for a set of points and areas, then outputs results and generates corresponding stress equations.

### Usage
1. Open `structs_stress_shear.m` in MATLAB.  
2. Run the script to compute centroid, moment of inertia, and stresses.

### Contents
* Calculation of centroid coordinates and shifting points to the centroid’s frame  
* Moment of inertia and shear/normal stresses  
* Display of results and stress equations

</details>
