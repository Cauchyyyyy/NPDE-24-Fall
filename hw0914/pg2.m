dx=0.02;
dt=0.01;

N=1/dt;
J=1/dx;
A=zeros(J,N);
j=1:J;
A(:,1)=sin(2*pi*(j-1)*dx);

% for j=1:J
%     A(j,1)=sin(2*pi*(j-1)*dx);
% end

% for n=2:N
%     for j=1:J
%         if j==J
%             A(j,n)=A(j,n-1)+dt/dx*(A(1,n-1)-A(j,n-1));
%         else
%             A(j,n)=A(j,n-1)+dt/dx*(A(j+1,n-1)-A(j,n-1));
%         end
%     end
% end

for n=2:N
    for j=1:J
        if j==J
            A(j,n)=A(j,n-1)+dt/dx*(A(1,n-1)-A(j-1,n-1))/2;
        elseif j==1
            A(j,n)=A(j,n-1)+dt/dx*(A(j+1,n-1)-A(J,n-1))/2;
        else
            A(j,n)=A(j,n-1)+dt/dx*(A(j+1,n-1)-A(j-1,n-1))/2;
        end
    end
end

x=0:dx:1;
x=x(1:50);
y=sin(2*pi*(x+0.3));
plot(x,y,x,A(:,31));
max(abs(y-A(:,31)));