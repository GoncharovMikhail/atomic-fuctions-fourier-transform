import numpy as np


def ft_up_m(m, t, nprod=20):
    powers_of_2m = np.power.outer(
        2 * m,
        np.linspace(1, nprod, nprod)
    )
    numerator = np.power(
        np.sinc(np.divide.outer(m * t, powers_of_2m) / np.pi),
        2
    )
    denominator = np.sinc(np.divide.outer(t, powers_of_2m) / np.pi)
    return np.prod(
        numerator / denominator,
        axis=1
    )
