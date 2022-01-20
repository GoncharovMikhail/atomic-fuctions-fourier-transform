import numpy as np


def ft_up(t, nprod=20):
    t = np.atleast_1d(t)
    p = np.power.outer(2, np.linspace(1, nprod, nprod))
    return np.prod(
        np.sinc(np.divide.outer(t, p) / np.pi),
        axis=1
    )
