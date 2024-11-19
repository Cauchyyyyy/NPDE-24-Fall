# %%
import matplotlib.pyplot
import numpy as np
from pde_solve import pde_solve

# %%
u=lambda x,t: np.piecewise((x-t) % 1,[(x-t) % 1<0.4,(x-t) % 1>0.6,((x-t) % 1>=0.4)&((x-t) % 1<=0.6)],[0,0,1])

x=np.linspace(0,1,100)

pde_solve(0.2)

pde_solve(0.8)

