import numpy as np

#todo!!!
def ft_fup_n(n, t, nprod=20):
    t = np.atleast_1d(t)
    p = np.power.outer(2, np.linspace(1, nprod, nprod))  # 2^p sinc(t/2^p)
    return np.multiply(
        np.power(
            np.sinc(np.divide(t, 2)), n
        ),
        np.prod(
            np.sinc(np.divide.outer(t, p) / np.pi),
            axis=1
        )
    )

#todo!!!
def fup_n(n, x, nsum=20, nprod=20):
    x = np.where(np.abs(x) <= (n + 2) / 2, x, 1)
    idx = np.linspace(1, nsum, nsum)
    coeff = ft_fup_n(n, np.pi * idx, nprod)
    return 2 / (n + 1) * (1 / 2 + np.sum(
        np.divide(coeff * np.cos(np.pi * np.multiply.outer(x, idx)), axis=1),
        (n + 1)
    )

                          )
