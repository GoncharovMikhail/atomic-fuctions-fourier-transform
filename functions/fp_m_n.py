import numpy as np

from fourier_tranform.fp_m_n import ft_fp_m_n


def fp_m_n(m, n, t, nsum=20, nprod=20):
    result = np.prod(
        2 / (n + 2),
        1 / 2 + np.sum(
            np.prod(
                # todo 2*np.pi*$$$k$$$ - k ?
                ft_fp_m_n(m, n, 2 * np.pi / (n + 2), nprod),
                np.cos(
                    # todo 2*np.pi*$$$k$$$*t - k ?
                    np.prod(2 * np.pi * t / (n + 2))
                )
            )
        )
    )
    return np.where(
        np.abs(result) <= (n + 2) / 2,
        result,
        0
    )
