import matplotlib
import numpy as np
import math

u=lambda x,t: np.sin(2*np.pi(x+t))

T=1
J=80
h=1/J
r=0.5
dt=r*h
x=np.arange(0,1,h)
v=np.zeros((J+1,int(T/dt)+1))
v[:,0]=u(x,0)
