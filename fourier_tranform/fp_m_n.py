import numpy as np

from fourier_tranform.up_m import ft_up_m


# todo dodelat
def ft_fp_m_n(m, n, t, nprod=20):
    coeff = np.prod(
        np.power(
            np.sinc(
                np.divide(t, 2),
                2
            ),
            m
        ),
        ft_up_m(n, t, nprod)
    )
    return np.prod(
        2 / (n + 2),
        np.sum(1)
    )
