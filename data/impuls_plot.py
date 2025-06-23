import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):

    def _multiple_formatter(x, pos):
        den = denominator
        num = int(np.rint(den * x / number))
        com = np.gcd(num, den)
        (num, den) = (int(num / com), int(den / com))
        if den == 1:
            if num == 0:
                return r'$0$'
            if num == 1:
                return r'$%s$' % latex
            elif num == -1:
                return r'$-%s$' % latex
            else:
                return r'$%s%s$' % (num, latex)
        else:
            if num == 1:
                return r'$\frac{%s}{%s}$' % (latex, den)
            elif num == -1:
                return r'$\frac{-%s}{%s}$' % (latex, den)
            else:
                return r'$\frac{%s%s}{%s}$' % (num, latex, den)
    return _multiple_formatter


class Multiple:
    def __init__(self, denominator=2, number=np.pi, latex='\pi'):
        self.denominator = denominator
        self.number = number
        self.latex = latex

    def locator(self):
        return plt.MultipleLocator(self.number / self.denominator)

    def formatter(self):
        return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))


def f_ind(
    t: npt.NDArray[np.float64],
    n: int,
    m: float,
    r: float,
    omega: float,
) -> npt.NDArray[np.float64]:
    return 2 * n * m * omega ** 2 * r * np.cos(omega * t)


def impulse_function(
    t: npt.NDArray[np.float64],
    n: int,
    m: list[float],
    r: list[float],
    omega_0: float,
) -> npt.NDArray[np.float64]:
    omega = omega_0 * np.arange(1, n + 1).reshape(-1, 1)
    m_matrix = np.array(m).reshape(-1, 1)
    r_matrx = np.array(r).reshape(-1, 1)
    t_matrix = np.tile(t, (n, 1))
    return (m_matrix * omega ** 2 * r_matrx * np.cos(omega * t_matrix)).sum(axis=0)


m = [
    2.75758026171761,
    0.969494952543874,
    0.486348994233291,
    0.273755006621712,
    0.155229853500278,
    0.076567059516108,
]
r = [
    0.020070401444444,
    0.011900487555556,
    0.008428804666667,
    0.006323725555556,
    0.004761892666667,
    0.003344359555556,
]

t = np.linspace(-np.pi, np.pi, 1000)
vibration = f_ind(t=t, n=1, m=m[0], r=r[0], omega=1)
impulse = impulse_function(t=t, n=6, m=m, r=r, omega_0=1)

fig, ax = plt.subplots(1, 1)
ax.set_ylabel("Движущая сила", fontsize=22)
ax.set_xlabel("Время", fontsize=22)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

ax.axhline(linewidth=1, color='k')
ax.axvline(linewidth=1, color='k')
ax.plot(
    t, vibration,
    color='r',
    label=r'для $N = 1$',
    linewidth=3,
)
ax.plot(
    t, impulse,
    color='g',
    label=r'для $N = 6$',
    linewidth=3,
)

plt.xticks(fontsize=22)
plt.grid(True)
plt.legend()
plt.show()
