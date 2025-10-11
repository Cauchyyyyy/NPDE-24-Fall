import numpy as np
import matplotlib.pyplot

u = lambda x, t: np.sin(2 * np.pi * (x + t))


def sol_CTCS(r: float, J: int, T: float):
    h = 1 / J
    dt = r * h
    x = np.arange(0, 1, h)  # which means [0,1) with step h
    v = np.zeros((J, int(T / dt)))
    v[:, 0] = u(x, 0)

    # v^1 for FTCS
    for j in range(-1, J - 1):
        v[j, 1] = v[j, 0] + r / 2 * (v[j + 1, 0] - v[j - 1, 0])

    # v^n, n>=2 for CTCS
    for n in range(2, int(T / dt)):
        for j in range(-1, J - 1):
            v[j, n] = v[j, n - 2] + r * (v[j + 1, n - 1] - v[j - 1, n - 1])

    matplotlib.pyplot.plot(x, u(x, T), x, v[:, int(T / dt) - 1])
    matplotlib.pyplot.legend(["exact", "approx"])
    matplotlib.pyplot.title(f"CTCS, r = {r}, t={T}, J={J}")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("u(x, t)")
    matplotlib.pyplot.savefig(f"CTCS, r = {r}, t={T}, J={J}.pdf")
    matplotlib.pyplot.show()


def sol_FTBS(r: float, J: int, T: float):
    h = 1 / J
    dt = r * h
    x = np.arange(0, 1, h)  # which means [0,1) with step h
    v = np.zeros((J, int(T / dt)))
    v[:, 0] = u(x, 0)

    # FTBS
    for n in range(1, int(T / dt)):
        for j in range(-1, J - 1):
            v[j, n] = v[j, n - 1] + r * (v[j, n - 1] - v[j - 1, n - 1])

    matplotlib.pyplot.plot(x, u(x, T), x, v[:, int(T / dt) - 1])
    matplotlib.pyplot.legend(["exact", "approx"])
    matplotlib.pyplot.title(f"FTBS, r = {r}, t={T}, J={J}")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("u(x, t)")
    matplotlib.pyplot.savefig(f"FTBS, r = {r}, t={T}, J={J}.pdf")
    matplotlib.pyplot.show()


if __name__ == "__main__":
    for r in [0.5, 1.5]:
        sol_CTCS(r, 80, 1.0)

    for J in [10, 20, 40, 80, 160]:
        sol_CTCS(0.5, J, 1.0)

    for T in [0.2, 0.5]:
        sol_FTBS(0.5, 80, T)
