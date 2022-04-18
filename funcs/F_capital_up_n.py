import numpy as np
from scipy import special

from funcs.up import up

#todo!!!
def Fup_n(n, x, nsum=20, nprod=20):
    return np.multiply(
        np.power(2, special.binom(n + 1, 2)),
        up(x - 1 + (n + 2) * pow(2, -n - 1), nsum, nprod)
    )
