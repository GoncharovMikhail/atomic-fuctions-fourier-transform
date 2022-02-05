import numpy as np


def ft_xi_n(n, t, nprod=20):
    powers_of_n_plus_1 = np.power.outer(
        n + 1,
        np.linspace(1, nprod, nprod)
    )
    tmp = np.power(
        np.sinc(np.divide.outer(t, powers_of_n_plus_1) / np.pi),
        n
    )
    return np.prod(
        tmp,
        axis=1
    )
