import numpy as np


def ft_cup(t, nprod=20):
    t = np.atleast_1d(t)
    powers_of_2 = np.power.outer(2, np.linspace(1, nprod, nprod))
    np.prod(np.sinc(t, powers_of_2))
    return np.prod(
        np.power(
            np.sinc(
                np.divide.outer(t, powers_of_2) / np.pi
            ),
            2
        ),
        axis=1
    )
