import numpy as np

from fourier_tranform.fup_n import ft_fup_n


def fup_m(m, x, nsum=20, npod=20):
    x = np.atleast_1d(x)
    np.linspace(-1.1, 1.1, nsum)
    result = 2 / (m + 2) * (
            # 1 / 2 + np.sum(ft_fup_n(m, 2 * np.pi * i / (m + 2), npod) * np.cos(2 * np.pi * i * x / (m + 2)))
    )
