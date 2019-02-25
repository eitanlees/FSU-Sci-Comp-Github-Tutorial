"""
Integration
-----------

A place to store methods related to integration.

Currently this file includes:
    - Trapizodial Rule
"""

import numpy as np

def left_riemann():
    return

def trapezoid(f, a, b, n):
    """Trapezoidal quadrature to estimate int x dx from a to b using n steps

    USAGE:
        x = trapezoidal(f, a, b, n)

    INPUT:
        f     - function to be integrated.
        a, b  - left and right boundaries respectively.
        n     - number of grid points

    OUTPUT:
        est   - estimation of the integral
    """
    x = np.linspace(a, b, n)
    est = 0
    for i in range(len(x) - 1):
        est += (x[i + 1] - x[i]) * (f(x[i]) + f(x[i + 1])) / 2
    return est

def simpson_13():
    return

def simpson_38():
    return
