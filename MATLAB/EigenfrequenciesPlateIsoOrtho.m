clear all
clc

% Calculation of the first four Eigenfrequencies 
% of a four-sided simply supported Kirchhoff-plate 
% for iso- or orthotropic material

%% ISO 

% Input Variables
Density=450;
E=1.061E+10;
nu=8.5E-02;  %nu_xy

thickness=0.04;         %thickness
length=3.45;%1.3;    %length
width=3;%1.1;       %width

% Calculcation
D=E*thickness^3/(12*(1-nu^2));
mu=Density*thickness;

omega = @(m,n) sqrt(D/mu)*((m*pi/length)^2+(n*pi/width)^2);

% Output
f=[omega(1,1),...
        omega(1,2),...
        omega(2,1),...
        omega(2,2)]/(2*pi)
    
%% ORTHO x=1, y=2

%Input Variables
Density=450;

E_x=1.061E+10;
E_y=7.605E+08;

G_xy=6.900E+08;%sqrt(488.9E+09*3.211E+08);

nu_x=6.1E-02;  %nu_xy
nu_y=18.4E-02; %nu_yx

thickness=0.04;         %thickness
length=3.45;%1.3;    %length
width=3;%1.1;       %width

% Calculation
D_x=E_x*thickness^2/(12*(1-nu_x*nu_y));
D_y=E_y*thickness^2/(12*(1-nu_x*nu_y));
D_k=G_xy*thickness^2/12;
D_xy=D_x*nu_y+2*D_k;

omega = @(m,n) pi^2/(length^2*sqrt(Density)) * sqrt(D_x*m^4+2*D_xy*m^2*n^2*(length/width)^2+D_y*n^4*(length/width)^4);

% Output
f=[omega(1,1),...
        omega(1,2),...
        omega(2,1),...
        omega(2,2)]/(2*pi)
    