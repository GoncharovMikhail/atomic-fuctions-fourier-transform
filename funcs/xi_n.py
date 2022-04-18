import numpy as np


def ft_xi_n(n, t, nprod=14):
    p = np.power.outer(n + 1, np.linspace(1, nprod, nprod))
    tmp = np.power(np.sinc(np.divide.outer(t, p) / np.pi), n)
    return np.prod(tmp, axis=1)


def xi_n(n, x, nsum=200):
    x = np.where(np.abs(x) <= 1, x, 1)
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_xi_n(n, np.pi * idx)
    return 1 / 2 + np.sum(coeff * np.cos(np.pi * np.multiply.outer(x, idx)), axis=1)
