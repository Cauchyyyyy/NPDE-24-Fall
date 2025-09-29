import numpy as np
import matplotlib.pyplot

u = lambda x, t: np.sin(2 * np.pi * (x + t))


def ndsolve(dt, T, method):
    dx = 0.02
    J = int(1 / dx)
    N = int(T / dt + 1)
    x = np.arange(0, 1, dx)
    v = np.zeros((J, N))
    v[:, 0] = u(x, 0)

    if method == "FTCS":
        r = dt / dx
        for n in range(1, N):
            for j in range(1, J - 1):
                v[j, n] = v[j, n - 1] + r * (v[j + 1, n - 1] - v[j - 1, n - 1]) / 2
            v[0, n] = v[0, n - 1] + r * (v[1, n - 1] - v[J - 1, n - 1]) / 2
            v[J - 1, n] = v[J - 1, n - 1] + r * (v[0, n - 1] - v[J - 2, n - 1]) / 2
    elif method == "FTFS":
        r = dt / dx
        for n in range(1, N):
            for j in range(0, J - 1):
                v[j, n] = v[j, n - 1] + r * (v[j + 1, n - 1] - v[j, n - 1])
            v[J - 1, n] = v[J - 1, n - 1] + r * (v[0, n - 1] - v[J - 1, n - 1])

    matplotlib.pyplot.plot(x, u(x, T), x, v[:, N - 1])
    matplotlib.pyplot.legend(["exact", "approx"])
    matplotlib.pyplot.title(f"dt={dt}, method={method}")
    matplotlib.pyplot.show()


if __name__ == "__main__":
    ndsolve(0.03, 0.3, "FTFS")
