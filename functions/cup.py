import numpy as np

from fourier_tranform.cup import ft_cup


def cup(t, nsum=20, nprod=20):
    sum_value = 1 / 2
    for k in 1, nsum:
        sum_value = sum_value + ft_cup(np.pi * k / 2, nprod) * np.cos(np.pi * k / 2 * t)
    return 1 / 2 * sum_value
