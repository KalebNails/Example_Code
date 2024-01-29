%Kaleb Nails
%Created: 9/~/22
% Modified 10/25/22


clc,clear, clearvars

%make a parabola based on two points, points above z before hitting ground.

f = figure('Name','Measured Data');

%Here are all the variables you can change by hand
Vxi = 10;
Vzi = 10;
x=0;
y=0;
z=0;
n = 1;
time = 0:.05:10;
ax = 33.0612;
%This controls the density of calculated points
timestep = .1;
testlength = 4;

%This is the gravity of the simulated work in m/s^2
g = 9.8;


%This gives the launcher its initial position
x_Launcher = 0;
y_Launcher = 0;
z_Launcher = 0;

%This gives the launcher its initial velocity
V_Launcher = 18;

%Sets up where the incoming projectile will start firing from
x0_incoming = 10;
y0_incoming = 20;
z0_incoming = 20;

%This sets up the initial velocity of the incoming projectile
Vx_incoming = -3;
Vy_incoming = -3;
Vz_incoming = 5;

%This sets up the position equation for the incoming projectile over time
x_incoming = Vx_incoming*time + x0_incoming;
y_incoming = Vy_incoming*time + y0_incoming;
z_incoming = Vz_incoming*time + z0_incoming - .5*g*time.^2;

%Do not change these constant values


%These are the equations:
%This creates the envelope shape
[Xdome,Ydome] = meshgrid(-40:10:40,-40:10:40);
Zdome = (V_Launcher^2)/(2*g)-g/(2*V_Launcher^2)*(Xdome.^2+Ydome.^2);
surf(Xdome,Ydome,Zdome,'FaceAlpha',.2)



%solve for what time it intercepts
syms t_collide
t_collide = solve((V_Launcher^2)/(2*g)-g/(2*V_Launcher^2)*((Vx_incoming*t_collide + x0_incoming)^2+(Vy_incoming*t_collide + y0_incoming)^2)-(Vz_incoming*t_collide + z0_incoming - .5*g*t_collide^2),t_collide);

%Gets rid of any negative times
t_collide = t_collide(t_collide >= 0);
%Picks the soonest collision
t_collide = min(t_collide);
fprintf('flight time = %f.2 \n',t_collide)
%calculate the collision point
xyz_collide = [Vx_incoming*t_collide + x0_incoming,Vy_incoming*t_collide + y0_incoming,Vz_incoming*t_collide + z0_incoming - .5*g*t_collide^2];
fprintf(' location = %f.2 \n',xyz_collide)
%find the angle between the launcher and the point of interception.
%finds the distance between the launcher and interception 
radius(1) = xyz_collide(1) - x_Launcher;
radius(2) = xyz_collide(2) - y_Launcher;
radius(3) = xyz_collide(3) - z_Launcher;
Collision_Distance = sqrt(sum(radius.^2));
%gives the unit vector between the collision point and origin
UnitV_radius = radius(:)/Collision_Distance;

%Gives the unit vector of the shadow vector cast by radius onto the
%xy-plane
V_radius_shadow = [radius(1),radius(2),0];
UnitV_radius_shadow = V_radius_shadow(:)/sqrt(sum(V_radius_shadow.^2));


syms Launch_angle
Launch_angle = solve(V_Launcher*sind(Launch_angle)*(sqrt(sum(V_radius_shadow(:).^2))/(V_Launcher*cosd(Launch_angle)))-.5*g*(sqrt(sum(V_radius_shadow(:).^2))/(V_Launcher*cosd(Launch_angle)))^2-radius(3),Launch_angle);
%get rid of negative and imaginary launch angles
%fprintf('%.2f \n',Launch_angle(1))
%fprintf('%.2f \n',Launch_angle(2))
%fprintf('%.2f \n',Launch_angle(3))

fprintf('vshadow = %f.3 \n', sqrt(sum(V_radius_shadow(:).^2)))

t_travel = sqrt(sum(V_radius_shadow(:).^2))/(V_Launcher*cosd(Launch_angle(:)));
t_travel = nonzeros(t_travel);
fprintf('angle = %f.3 \n', Launch_angle)
fprintf('time = %f.3 \n', t_travel)

%Now we find where horizontally it should aim
syms Launch_z
Launch_z = solve(Launch_z/sqrt(sum(V_radius_shadow(:).^2)) -tand(Launch_angle));

%create a unit vetor of where to aim
to_aim = [V_radius_shadow(1),V_radius_shadow(2),Launch_z];
to_aim = to_aim./sqrt(sum(to_aim(:).^2));

x_Launcher = x_Launcher + to_aim(1)*V_Launcher*time;
y_Launcher = y_Launcher + to_aim(2)*V_Launcher*time;
z_Launcher = z_Launcher + to_aim(3)*V_Launcher*time -.5*g*time.^2;

%Launch_direction = [UnitV_radius(1),UnitV_radius(2),sdfkjdfsjkldfskjldfsakjlfdsa];

%fprintf('%.2f \n',t_travel(1))
%fprintf('%.2f \n',t_travel(2))
%fprintf('%.2f \n',t_travel(3))





axis([-ax ax -ax ax 0 ax])
hold on
grid on 
plot3(x_incoming,y_incoming,z_incoming,'r*','MarkerSize',2)
hold on 

axis([-ax ax -ax ax 0 ax])

%plots point of interception

plot3(xyz_collide(1),xyz_collide(2),xyz_collide(3),'b*','MarkerSize',30)

hold on
axis([-ax ax -ax ax 0 ax])
plot3(x_Launcher,y_Launcher,z_Launcher,'g*','MarkerSize',4)


