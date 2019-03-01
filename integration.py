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
    """Trapezoidal quadrature to estimate int x dx from a to b using n uniform steps

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
    dx = x[1] - x[0]

    summation = np.sum(f(x[1:-1]))
    est = (dx / 2) * (f(a) + 2 * summation + f(b))
    return est


def simpson_13():
x = np.linsapce(a,b,n)
h = (b-a) / n

summation = 0

for i in range n:
	if(i<n):

	if (i < n-1):

return h / 3.0 * (b[0] + y[n] + summation
    return


def simpson_38():
    return
