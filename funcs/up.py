import numpy as np


def ft_up(t, nprod=20):
    t = np.atleast_1d(t)
    p = np.power.outer(2, np.linspace(1, nprod, nprod))  # 2^p sinc(t/2^p)
    return np.prod(np.sinc(np.divide.outer(t, p) / np.pi), axis=1)


def up(x, nsum=100, nprod=20):
    x = np.atleast_1d(x)
    x = np.where(np.abs(x) <= 1, x, 1)
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_up(np.pi * idx, nprod)
    return 1 / 2 + np.sum(coeff * np.cos(np.pi * np.multiply.outer(x, idx)), axis=1)
