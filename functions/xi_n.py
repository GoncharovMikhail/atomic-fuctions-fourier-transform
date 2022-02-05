import numpy as np

from fourier_tranform.xi_n import ft_xi_n


def xi_n(n, t, nsum, nprod):
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_xi_n(n, np.pi * idx, nprod)
    result = 1 / 2 + np.sum(
        coeff * np.cos(np.pi * np.multiply.outer(t, idx)),
        axis=1
    )
    return np.where(
        np.abs(result) < 1,
        result,
        0
    )
