u=@(x,t) sin(2*pi*(x+t));
r=0.5;
J=[10,20,40,80,160];
h=1./J;
T=1;
dt=r*h;

for j=1:length(J)
    v=ndsolve(r,J(j),2);
    x=0:h(j):1;x=x';
    exact=u(x,T);
    plot(x,v(:,end),'-o');
    
    hold on;
end
plot(x,exact,'r');
hold off;
legend('J=10','J=20','J=40','J=80','J=160','exact');