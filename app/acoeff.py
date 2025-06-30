import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def impulse_function(
    t: npt.NDArray[np.float64],
    n: int,
    m: list[float],
    r: list[float],
    omega_0: float,
    deb: int,
    noise_power: float,
) -> npt.NDArray[np.float64]:
    omega = omega_0 * np.arange(1, n + 1).reshape(-1, 1)
    noise = np.ones(n)
    noise[deb] -= 1 * noise_power
    noise = noise.reshape(-1, 1)
    # m_matrix = np.array(m).reshape(-1, 1)
    # r_matrx = np.array(r).reshape(-1, 1)
    t_matrix = np.tile(t, (n, 1))
    x = np.array(range(n, 0, -1)).reshape(-1, 1)
    # return (m_matrix * (omega * noise) ** 2 * r_matrx * np.cos(omega * noise * t_matrix)).sum(axis=0)
    return (x * np.cos(omega * t_matrix * noise)).sum(axis=0)


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

n = 8
# m = [(n - k + 1) for k in range(1, 7)]

# t = np.linspace(-np.pi, np.pi, 1000)
# vibration = f_ind(t=t, n=1, m=m[0], r=r[0], omega=1)
# impulse = impulse_function(t=t, n=6, m=m, r=r, omega_0=1)


def func(x, y):
    t = np.linspace(-np.pi, np.pi, 10000)
    impulse = impulse_function(t=t, n=n, m=m, r=r, omega_0=1, deb=x, noise_power=y)
    return np.abs(np.max(impulse) / np.min(impulse))


fig, ax = plt.subplots(1, 1)
ax.set_ylabel(fr"Коэффициент асимметрии $K_{n}$ ({n} пар дебалансов)", fontsize=14)
ax.set_xlabel("Ошибка в угловой скорости вращения", fontsize=14)
ax.set_xscale("log")

noise_power = np.array([10 ** -x for x in range(3, 8)])
# noise_power = np.array([10 ** -1, 5 * 10 ** -2, 10 ** -2, 5 * 10 ** -3, 10 ** -3, 5 * 10 ** -4, 10 ** -4, 5 * 10 ** -5, 10 ** -5, 10 ** -6])
for d in range(n):
    deb_text = {
        3: 'я',
    }.get(d + 1, 'ая')
    ax.plot(
        noise_power,
        [func(d, p) for p in noise_power],
        # label=fr'${d + 1}^{{{deb_text}}}$ пара дебалансов с дефектами',
        label=fr'{d + 1}-{deb_text} пара дебалансов с дефектами',
        linestyle='--',
        marker='o',
    )

plt.legend()
plt.grid(True)
plt.show()
