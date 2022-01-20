import numpy as np

from fourier_tranform.up import ft_up


def up(x, nsum=100):
    x = np.atleast_1d(x)
    x = np.where(np.abs(x) <= 1, x, 1)
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_up(np.pi * idx)
    return 1 / 2 + np.sum(
        coeff * np.cos(np.pi * np.multiply.outer(x, idx)),
        axis=1
    )
