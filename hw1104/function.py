import matplotlib.pyplot
import numpy as np

u=lambda x,t: np.piecewise((x-t) % 1,[(x-t) % 1<0.4,(x-t) % 1>0.6,((x-t) % 1>=0.4)&((x-t) % 1<=0.6)],[0,0,1])

x0=np.linspace(0,1,100)

def pde_solve(r):
# %%
    T=3.5
    h=0.05
    J=int(1/h)

    dt=r*h
    N=round(T/dt)
    x=np.arange(0,1,h)  # which means [0,1) with step h

    # %%
    # FTBS
    v_ftbs=np.zeros((J,N))
    v_ftbs[:,0]=u(x,0)
    for n in range(1,N):
        for j in range(J):
            v_ftbs[j,n]=v_ftbs[j,n-1]-r*(v_ftbs[j,n-1]-v_ftbs[(j-1)%J,n-1])

    # %%
    # FTCS
    v=np.zeros((J,N))
    v[:,0]=u(x,0)
    for n in range(1,N):
        for j in range(1,J-1):
            v[j,n]=v[j,n-1]-r/2*(v[j+1,n-1]-v[j-1,n-1])
        v[0,n]=v[0,n-1]-r/2*(v[1,n-1]-v[J-1,n-1])
        v[J-1,n]=v[J-1,n-1]-r/2*(v[0,n-1]-v[J-2,n-1])

    # %%
    # Lax-Wendroff
    v_lw=np.zeros((J,N))
    v_lw[:,0]=u(x,0)
    for n in range(1,N):
        for j in range(1,J-1):
            v_lw[j,n]=v_lw[j,n-1]-r/2*(v_lw[j+1,n-1]-v_lw[j-1,n-1])+r**2/2*(v_lw[j+1,n-1]-2*v_lw[j,n-1]+v_lw[j-1,n-1])
        v_lw[0,n]=v_lw[0,n-1]-r/2*(v_lw[1,n-1]-v_lw[J-1,n-1])+r**2/2*(v_lw[1,n-1]-2*v_lw[0,n-1]+v_lw[J-1,n-1])
        v_lw[J-1,n]=v_lw[J-1,n-1]-r/2*(v_lw[0,n-1]-v_lw[J-2,n-1])+r**2/2*(v_lw[0,n-1]-2*v_lw[J-1,n-1]+v_lw[J-2,n-1])

    # %%
    i=0
    for t in [0.05,0.2,0.8,3.2]:
        matplotlib.pyplot.figure(1)
        i=i+1
        matplotlib.pyplot.subplot(2,2,i)
        matplotlib.pyplot.plot(x0,u(x0,t),x,v_lw[:,round(t/dt)],x,v[:,round(t/dt)],x,v_ftbs[:,round(t/dt)])
        matplotlib.pyplot.legend(['exact','Lax-Wendroff','FTCS','FTBS'])
        matplotlib.pyplot.title(f'r={r},t={t}')


    # %%
    i=0
    for t in [0.8,3.2]:
        matplotlib.pyplot.figure(2)
        i+=1
        matplotlib.pyplot.subplot(1,2,i)
        matplotlib.pyplot.plot(x0,u(x0,t),x,v_lw[:,round(t/dt)],x,v_ftbs[:,round(t/dt)])
        matplotlib.pyplot.legend(['exact','Lax-Wendroff','FTBS'])
        matplotlib.pyplot.title(f'r={r},t={t}')
        
    matplotlib.pyplot.show()