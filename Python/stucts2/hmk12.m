clear;clc;
syms pt16 pb16 pt23 pb23 pt34 pb34 pl45 pl36 pt56 pb56 y1 y2 y5 y6 x5 x6 q1 q2

pr45 = 0;


eqn1 = y1 == pt16;%
eqn17 = pt16+9*q1 == pb16;%
eqn14 = pt23 == 9*q1+pb23;%
eqn3= y2==pt23;%
eqn5 = pb23 ==pt34;%
eqn15 = 0 ==pt34-12*q2-pb34;
eqn9 = pb56 ==-y5;
eqn18 = pt56 + 12*q2 == pb56;%
eqn10 = pl45 ==x5;
eqn13 = 0 ==40*q2 + pr45-pl45;
eqn11 = pl36 == -x6;
eqn16 = 2500+40*q1 == 40*q2 + pl36;
eqn12 = 0 == y6+pb16-pt56;

equations = [eqn1, eqn3, eqn5, eqn9, eqn10, eqn11, eqn12, eqn13, eqn14, eqn15, eqn16, eqn17, eqn18];
variables = [pt16, pb16, pt23,pb23, pt34, pb34, pl36, pt56, pb56, y2, y5, q1,q2,pl45];
% all of them variables = [pt16, pb16, pt23, pb23, pt34, pb34, pl36, pt56, pb56, y2, y5, y6, x5, x6, q1,q2,pl45,y1];

% Solve the equations
[pt16, pb16, pt23,pb23, pt34, pb34, pl36, pt56, pb56, y2, y5, q1,q2,pl45] = solve(equations, variables)

%now deal with virtuals and hardcode them:
syms dpt16 dpb16 dpt23 dpb23 dpt34 dpb34 dpl45 dpl36 dpt56 dpb56 dy1 dy2 dy5 dy6 dx5 dx6 dq1 dq2

dpr45 = 0;


deqn1 = dy1 == dpt16;%
deqn17 = dpt16+9*dq1 == dpb16;%
deqn14 = dpt23 == 9*dq1+dpb23;%
deqn3= dy2==dpt23;%
deqn5 = dpb23 ==dpt34;%
deqn15 = 0 ==dpt34-12*dq2-dpb34;
deqn9 = dpb56 ==-dy5;
deqn18 = dpt56 + 12*dq2 == dpb56;%
deqn10 = dpl45 ==dx5;
deqn13 = 0 ==40*dq2 + dpr45-dpl45;
deqn11 = dpl36 == -dx6;
deqn16 = 40*dq1 == 40*dq2 + dpl36;
deqn12 = 0 == dy6+dpb16-dpt56;

dequations = [deqn1, deqn3, deqn5, deqn9, deqn10, deqn11, deqn12, deqn13, deqn14, deqn15, deqn16, deqn17, deqn18];
dvariables = [dpt16, dpb16, dpt23,dpb23, dpt34, dpb34, dpl36, dpt56, dpb56, dy2, dy5, dq1,dq2,dpl45];
% all of them variables = [pt16, pb16, pt23, pb23, pt34, pb34, pl36, pt56, pb56, y2, y5, y6, x5, x6, q1,q2,pl45,y1];

% Solve the equations
[dpt16, dpb16, dpt23,dpb23, dpt34, dpb34, dpl36, dpt56, dpb56, dy2, dy5, dq1,dq2,dpl45] = solve(dequations, dvariables)

%plug in known values:
pr36 = 2500;
pb34 = 2400;
pr45 = 0;


%now solve the stiffeners
stiff12 = 9*((2*pt16+pb16)*dpt16+(pt16+2*pb16)*dpb16)
stiff23 = 9*((2*pt23+pb23)*dpt23+(pt23+2*pb23)*dpb23)
stiff36 = 40*(2*pl36+pr36)*dpl36
stiff56 = 12*(2*pt56+pb56)*dpt56
stiff34 = 12*(2*pt34+pb34)*dpt34
stiff45 = 40*(2*pl45+pr45)*dpl45


A = .4; E = 14.9*10^6;
du_stiff = (stiff12 + stiff23 + stiff36 + stiff56 + stiff34 + stiff45)/(6*E*A)

%collected_du_stiff =collect(du_stiff,[dx5,dx6,dy1,dy2])

%now get the shear panels
Panel1 = 9*40*q1*dq1
Panel2 = 40*12*q2*dq2

G =5.7*10^6 ; t= 0.095;%known terms
du_shear = (Panel1+Panel2)/(G*t)

full_eq = du_shear + du_stiff;
collected_terms = vpa(collect(full_eq,[dx5,dx6,dy1,dy2]),4)

%now solve for the 4 redunants:
feqn1 = 0 == vpa("11.7")*x5 - vpa("8.1")*x6 + vpa("36.0")*y1 + vpa("36.0")*y6 - vpa("20250.0");
feqn2 = 0 ==  (vpa("4.971e-7")*x5 - vpa("3.964e-7")*x6 + vpa("2.517e-6")*y1 + vpa("1.007e-6")*y6 - vpa("0.000991"));
feqn3 = 0 == (vpa("5.741e-7")*x5 - vpa("2.789e-6")*x6 + vpa("3.964e-7")*y1 + vpa("2.265e-7")*y6 + vpa("0.001237"));
feqn4 = 0 == vpa("3.365e-6")*x5 - vpa("5.514e-7")*x6 + vpa("3.964e-7")*y1 + vpa("2.265e-7")*y6 - vpa("0.00156");

fvariables = [x5,x6,y1,y6];
feqn = [feqn1,feqn2,feqn3,feqn4];
[fx5,fx6,fy1,fy6] = solve(feqn,fvariables)

final_subs = [pt16, pb16, pt23,pb23, pt34, pl36, pt56, pb56, y2, y5, q1,q2,pl45];
answers=vpa(subs(final_subs,[x5,x6,y1,y6],[fx5,fx6,fy1,fy6]),3);
disp(answers)

