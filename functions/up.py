import numpy as np

from fourier_tranform.up import ft_up


def up(x, nsum=100):
    x = np.atleast_1d(x)
    result = 1 / 2 + np.sum(
        ft_up(np.pi * np.linspace(1, nsum, nsum)) * np.cos(np.pi * np.multiply.outer(x, np.linspace(1, nsum, nsum))),
    )
    return np.where(
        np.abs(x) < 1,
        result,
        0
    )
