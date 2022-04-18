import numpy as np


def ft_h_a(a, t, nprod=10):
    p = np.power.outer(a, np.linspace(1, nprod, nprod))
    return np.prod(np.sinc(np.divide.outer(t, p) / np.pi), axis=1)


def h_a(a, x, nsum=100, nprod=10):
    x = np.where(np.abs(x) <= 1 / (a - 1), x, 1 / (a - 1))
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_h_a(a, (a - 1) * np.pi * idx, nprod)
    return (a - 1) * (1 / 2 + np.sum(coeff * np.cos(np.pi * np.multiply.outer((a - 1) * x, idx)), axis=1))
