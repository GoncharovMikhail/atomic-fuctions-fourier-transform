import numpy as np

from fourier_tranform.fup_m import ft_fup_m

#
#def fup_m(m, t, nsum=20, npod=20):
#    t = np.atleast_1d(t)
#    result = np.sum(
#        2 / (m + 2),
#todo следующая строчка, не пойму, как это ее правильно написать
#        1 / 2 + np.sum(ft_fup_m(m, 2 * np.pi * i / (m + 2), npod) * np.cos(2 * np.pi * i * t / (m + 2)))
#    )
