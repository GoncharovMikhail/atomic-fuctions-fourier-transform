import numpy as np

from fourier_tranform.up_m import ft_up_m


def up_m(m, t, nsum=20, nprod=20):
    idx = np.linspace(1, nsum, nsum)
    result = 1 / 2 + np.sum(
        ft_up_m(m, np.pi * idx, nprod) * np.cos(np.pi * np.multiply.outer(t, idx)),
        axis=1
    )
    return np.where(
        np.abs(t) < 1,
        result,
        0
    )
