m=[20,160];
N=[10,100];

resultshow(160,10);

function resultshow(m,N)
v=@(x) (pi-x)/2;
u=@(x,omega) sin(omega*x)/omega;
uu=@(x,omega,n) sin(omega*pi/n)*n*sin(omega*x)/(omega^2*pi);

x1=0:2*pi/m:2*pi;
y1=zeros(1,length(x1));
y2=zeros(1,length(x1));

for n=1:N
    y1=y1+u(x1,n);
    y2=y2+uu(x1,n,N);
end
plot(x1,v(x1),x1,y1,x1,v(x1)-y1,x1,y2,x1,v(x1)-y2);
legend('v','v_N','v-v_N','v_N^~','v-v_N^~');
title(['m=',num2str(m),',N=',num2str(N)]);

end