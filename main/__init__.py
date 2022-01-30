import numpy as np
from matplotlib import pyplot as plt

from functions.up import up

if __name__ == "__main__":
    nx = 2 ** 14
    x = np.linspace(-1.1, 1.1, nx)
    y = up(x)

    # todo не работает
    # plt.figure()
    # plt.plot(x, y)
