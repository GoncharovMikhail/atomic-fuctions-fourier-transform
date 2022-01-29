import numpy as np


def ft_cup(t, nprod=20):
    prod = 1
    for i in 1, nprod:
        prod = prod*np.sinc(t)**2
    return prod
