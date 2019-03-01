"""
Linear Algebra
-----------

A place to store methods related to linear algebra.

Currently this file includes:
    - Weighted Jacobi method
"""

import numpy as np

# Iterative Methods


def jacobi(A, x, b):
    return x


def weighted_jacobi(A, x, b, omega=2 / 3, max_iter=1000):
    """Weighted Jacobi method for finding the approximate solution of Ax=b

        USAGE:
            sol = weighted_jacobi(A, x, b)

        INPUT:
            A     - matrix of size (n, n)
            x     - initial guess of the solution
            b     - right hand side of the equation

        OUTPUT:
            x     - estimation of the solution
        """
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Check to see if iteration has converged
        if np.allclose(x, x_new, atol=1e-10, rtol=0.0):
            break

        # Replace x with weight of omega
        x = omega * x_new + (1 - omega) * x

    return x


def gauss_seidel(A, x, b):
    return x


def sor(A, x, b):
    return x
