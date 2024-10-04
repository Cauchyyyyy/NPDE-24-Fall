u=@(x,t) sin(2*pi*(x+t));

J=80;
h=1/J;

x=0:1/J:1;x=x';

v1=ndsolve(0.5,J);
dt1=h*0.5;
v2=ndsolve(1.5,J);
dt2=h*1.5;


T=1;
tiledlayout('flow');
nexttile;
plot(x,u(x,T),x,v1(:,cast(1/dt1+1,'int64')),'-o');
legend('u(x,T)','r=0.5');
nexttile;
plot(x,u(x,T),x,v2(:,cast(1/dt2+1,'int64')),'-o');
legend('u(x,T)','r=1.5');