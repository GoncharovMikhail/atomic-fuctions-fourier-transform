import numpy as np
import scipy.special

from functions.up import up


def Fup_n(n, x):
    x = np.atleast_1d(x)
    x = np.where(np.abs(x) <= (n + 2) / pow(2, n), x, 1)
    # todo check
    return np.power(2, scipy.special.binom(2, n + 1)) * up(x - 1 + (n - 2) * pow(2, -n - 1))
