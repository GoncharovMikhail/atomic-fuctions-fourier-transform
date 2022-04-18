import numpy as np

from funcs.up_m import ft_up_m


def ft_fup_m_n(m, n, t, nprod=20):
    coeff = np.power(np.sinc(np.divide(t, 2)), n)
    return np.multiply(
        coeff,
        ft_up_m(m, t, nprod)
    )


# todo!!!
def fup_m_n(m, n, t, nsum=20, nprod=20):
    return np.multiply(2 / (n + 2), 1 / 2 + np.sum(4, 4))
