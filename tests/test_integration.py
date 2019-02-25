import numpy as np
from integration import *


def test_trapezoid():
    func = lambda x: np.sin(x)
    est_I = trapezoid(func, 0, np.pi, 2000)
    true_I = 2.0
    assert np.isclose(est_I, true_I)
