import numpy as np
from linalg import *


def test_weighted_jacobi():
    # initialize the matrix
    A = np.array(
        [
            [10.0, -1.0, 2.0, 0.0],
            [-1.0, 11.0, -1.0, 3.0],
            [2.0, -1.0, 10.0, -1.0],
            [0.0, 3.0, -1.0, 8.0],
        ]
    )
    # initialize the RHS vector
    b = np.array([6.0, 25.0, -11.0, 15.0])

    # initialize guess
    x = np.zeros_like(b)

    wj_x = weighted_jacobi(A, x, b)

    assert np.allclose(wj_x, np.linalg.inv(A).dot(b))
