import numpy as np


def ft_up_m(m, t, nprod=20):
    prod = 1
    for i in 1, nprod:
        prod = prod * np.sinc(m * t / (2 * m) ** i) ** 2 / np.sinc(t / (2 * m) ** i)
    return prod
