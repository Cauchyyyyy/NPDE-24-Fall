function v=ndsolve(r,J,method)
h=1/J;
x=0:h:1;
dt=r*h;
v=zeros(J+1,1/dt+1);
v(:,1)=sin(2*pi*x);

if method==1 % FTCS
    for n=1:1/dt
        for j=2:J
            v(j,n+1)=v(j,n)+r/2*(v(j+1,n)-v(j-1,n));
        end
        v(1,n+1)=v(1,n)+r/2*(v(2,n)-v(J,n));
        v(J+1,n+1)=v(1,n+1);
    end
elseif method==2 % Lax-Wendroff
    for n=1:1/dt
        for j=2:J
            v(j,n+1)=v(j,n)+r/2*(v(j+1,n)-v(j-1,n))+r^2/2*(v(j+1,n)-2*v(j,n)+v(j-1,n));
        end
        v(1,n+1)=v(1,n)+r/2*(v(2,n)-v(J,n))+r^2/2*(v(2,n)-2*v(1,n)+v(J,n));
        v(J+1,n+1)=v(1,n+1);
    end
elseif method==3 % Lax-Friedrichs
    for n=1:1/dt
        for j=2:J
            v(j,n+1)=v(j,n)+r/2*(v(j+1,n)-v(j-1,n))+1/2*(v(j+1,n)-2*v(j,n)+v(j-1,n));
        end
        v(1,n+1)=v(1,n)+r/2*(v(2,n)-v(J,n))+1/2*(v(2,n)-2*v(1,n)+v(J,n));
        v(J+1,n+1)=v(1,n+1);
    end
else
    disp('Invalid method');
    return;
end
end