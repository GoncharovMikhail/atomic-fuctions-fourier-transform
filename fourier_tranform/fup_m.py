import numpy as np


def ft_fup_m(m, t, nprod=20):
    t = np.atleast_1d(t)
    powers_of_2 = np.power.outer(2, np.linspace(1, nprod, nprod))
    coeff = np.power(np.sinc(np.divide(t, 2)), m)
    return coeff * np.prod(
        np.sinc(np.divide.outer(t, powers_of_2) / np.pi),
        axis=1
    )
