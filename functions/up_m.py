import numpy as np

from fourier_tranform.up_m import ft_up_m


def up_m(m, t, nsum=20, nprod=20):
    sum_value = 1 / 2
    for i in 1, nsum:
        sum_value = sum_value + ft_up_m(m, np.pi * i, nprod) * np.cos(np.pi*i*t)
    return sum_value
