# %%
import numpy as np
import matplotlib.pyplot as plt

u_exact = lambda x, t: np.sin(2 * np.pi * (x + t))

# x \in [0,1], t \in [0,T]
dx = 0.02
dt = 0.03

T = 0.3
x = np.linspace(0, 1, int(1 / dx), endpoint=False)
J = len(x)
u1 = np.zeros((len(x), int(T / dt) + 1))
u2 = np.zeros((len(x), int(T / dt) + 1))
u3 = np.zeros((len(x), int(T / dt) + 1))
# Initial condition
u1[:, 0] = u_exact(x, 0)
u2[:, 0] = u_exact(x, 0)
u3[:, 0] = u_exact(x, 0)

# Periodic boundary condition
# FTFS scheme
for n in range(0, int(T / dt)):
    for j in range(-1, J-1):
        u1[j, n + 1] = u1[j, n] + dt / dx * (u1[j + 1, n] - u1[j, n])
# FTBS scheme
        u2[j, n + 1] = u2[j, n] + dt / dx * (u2[j, n] - u2[j - 1, n])
# FTCS scheme
        u3[j, n + 1] = u3[j, n] + dt / (2 * dx) * (u3[j + 1, n] - u3[j - 1, n])
# Plotting
plt.plot(x, u_exact(x, T), label='Exact')
plt.plot(x, u1[:, -1], '-.', label='FTFS')
plt.plot(x, u2[:, -1], '-o', label='FTBS')
plt.plot(x, u3[:, -1], '<', label='FTCS')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('dx=%.2f, dt=%.2f, T=%.2f' % (dx, dt, T))
plt.legend()
plt.savefig('dt%.2f.pdf' % dt)
plt.show()


