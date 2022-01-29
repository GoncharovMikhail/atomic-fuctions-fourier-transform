import numpy as np


def ft_eup_a(a, t, nprod=20):
    prod = 1
    for k in 1, nprod:
        prod = prod * shc(np.log(a) / 2 * t - 1j * t * 2 ** -k) / shc(np.log(a) / 2)
    return prod


def shc(t):
    return np.sinh(t) / t
