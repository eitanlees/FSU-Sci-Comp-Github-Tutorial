import numpy as np
from linalg import *

def test_weighted_jacobi():
    # initialize the matrix
    A = np.array([[10., -1., 2., 0.],
                  [-1., 11., -1., 3.],
                  [2., -1., 10., -1.],
                  [0.0, 3., -1., 8.]])
    # initialize the RHS vector
    b = np.array([6., 25., -11., 15.])

    # initialize guess
    x = np.zeros_like(b)

    wj_x = weighted_jacobi(A, x, b)

    assert np.allclose(wj_x, np.linalg.inv(A).dot(b))
