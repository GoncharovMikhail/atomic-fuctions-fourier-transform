import numpy as np
import scipy.special

from functions.up import up


# todo проверить
def Fup_n(n, x):
    result = np.prod(
        2 ** scipy.special.binom(n + 1, 2),
        up(x - 1 + (n + 2) * pow(2, -n - 1))
    )
    return np.where(
        np.abs(x) <= (n + 2) / 2 ** n,
        result,
        0
    )
