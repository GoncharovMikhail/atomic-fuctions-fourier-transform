import numpy as np


def ft_fup_n(n, t, nprod=20):
    prod = np.sinc(t/2)**n
    for i in 2, nprod:
        prod = prod * np.sinc(t/2**i)
    return prod
