import numpy as np


def ft_up_m(m, t, nprod=14):
    p = np.power.outer(2 * m, np.linspace(1, nprod, nprod))
    numerator = np.power(np.sinc(np.divide.outer(m * t, p) / np.pi), 2)
    denominator = np.sinc(np.divide.outer(t, p) / np.pi)
    return np.prod(numerator / denominator, axis=1)


def up_m(m, x, n=100):
    x = np.where(np.abs(x) <= 1, x, 1)
    idx = np.linspace(1, n, n)
    coeff = ft_up_m(m, np.pi * idx)
    return 1 / 2 + np.sum(coeff * np.cos(np.pi * np.multiply.outer(x, idx)), axis=1)
