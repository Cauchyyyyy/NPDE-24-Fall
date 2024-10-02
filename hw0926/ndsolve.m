function v=ndsolve(r,J)
% CTCS

h=1/J;
x=0:h:1;
dt=r*h;
v=zeros(J+1,cast(3/dt+1,'int64'));
v(:,1)=sin(2*pi*x);

for n=1:3/dt
    if n==1
        %FTCS
        for j=2:J
            v(j,n+1)=v(j,n)+r/2*(v(j+1,n)-v(j-1,n));
        end
        v(1,n+1)=v(1,n)+r/2*(v(2,n)-v(J,n));
        v(J+1,n+1)=v(1,n+1);
    else
        %CTCS
        for j=2:J
            v(j,n+1)=v(j,n-1)+r*(v(j+1,n)-v(j-1,n));
        end
        v(1,n+1)=v(1,n-1)+r*(v(2,n)-v(J,n));
        v(J+1,n+1)=v(1,n+1);
    end
end

end