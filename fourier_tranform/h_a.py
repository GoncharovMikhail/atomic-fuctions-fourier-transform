import numpy as np


def ft_h_a(a, t, nprod=10):
    powers_of_a = np.power.outer(
        a,
        np.linspace(1, nprod, nprod)
    )
    return np.prod(
        np.sinc(np.divide.outer(t, powers_of_a) / np.pi),
        axis=1
    )
