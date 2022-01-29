import numpy as np

from fourier_tranform.fup_n import ft_fup_n


def fup_n(n, t, nsum=20, npod=20):
    sum_value = 1 / 2
    for i in 1, nsum:
        sum_value = sum_value + ft_fup_n(n, 2 * np.pi * i / (n + 2), npod) * np.cos(2 * np.pi * i * t / (n + 2))
    return 2 / (n + 2) * sum_value
