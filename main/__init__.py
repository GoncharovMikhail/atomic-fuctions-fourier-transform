import matplotlib.pyplot as plt
import numpy as np

# todo еще не реализовано
#  pi_m(x)
#  fip_a,n(x)
#  ch_a,n(x)
#  eup_a(x)
from funcs.F_capital_up_n import Fup_n

# todo надо проверить реализацию
#  funcs.Fup_n

if __name__ == "__main__":
    nx = 2 ** 14
    x = np.linspace(-1.1, 1.1, nx)
    n = 6
    y = Fup_n(n, x)

    plt.figure()
    plt.plot(x, y)
