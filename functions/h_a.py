import numpy as np

from fourier_tranform.h_a import ft_h_a


def h_a(a, t, nsum=20, nprod=20):
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_h_a(a, (a - 1) * np.pi * idx, nprod)
    result = (a - 1) * (
            1 / 2 +
            np.sum(
                coeff * np.cos(np.pi * np.multiply.outer((a - 1) * t, idx)),
                axis=1
            )
    )
    return np.where(
        np.abs(result) <= 1 / (a - 1),
        result,
        0
    )
