u=@(x,t) sin(2*pi*(x+t));
r=0.5;
J=80;
h=1/J;
dt=r*h;
x=0:1/J:1;x=x';

v1=ndsolve(r,J,1);
v2=ndsolve(r,J,2);
v3=ndsolve(r,J,3);

T=[0,0.05,0.1,0.2,0.4,0.8,1];
errors=zeros(3,length(T));
for i=1:length(T)
    errors(1,i)=max(abs(v1(:,T(i)/dt+1)-u(x,T(i))));
    errors(2,i)=max(abs(v2(:,T(i)/dt+1)-u(x,T(i))));
    errors(3,i)=max(abs(v3(:,T(i)/dt+1)-u(x,T(i))));
end
plot(T,errors(1,:),'-o',T,errors(2,:),'-o',T,errors(3,:),'-o');
legend('FTCS','Lax-Wendroff','Lax-Friedrichs');