import decimal

import mpmath
import sys
import math
from decimal import Decimal, getcontext

sys.set_int_max_str_digits(500000)


def gauss_legendre_pi(iteration, precision):
    getcontext().prec = precision

    # Initialize variables
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    # Compute digits of PI
    for i in range(iteration):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t_next = t - p * (a - a_next) ** 2
        p = 2 * p
        a = a_next
        t = t_next

    # Calculate PI
    pi = (a + b) ** 2 / (4 * t)

    return pi


def machin_pi(precision):
    mpmath.mp.dps = precision
    pi = 4 * (4 * mpmath.atan(1 / 5) - mpmath.atan(1 / 239))
    return pi


def sqrt(n, one):
    """
 Return the square root of n as a fixed point number with the one
 passed in.  It uses a second order Newton-Raphson convergence.  This
 doubles the number of significant figures on each iteration.
 """
    # Use floating point arithmetic to make an initial guess
    floating_point_precision = 10 ** 16
    n_float = float((n * floating_point_precision) // one) / floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
    n_one = n * one
    while 1:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x


def chudnovsky_pi(one):
    """
    Calculate pi using Chudnovsky's series

    This calculates it in fixed point, using the value for one passed in
    """
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    C = 640320
    C3_OVER_24 = C**3 // 24
    while 1:
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*C3_OVER_24
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi_c = (426880*sqrt(10005*one, one)*one) // total
    len_c = len(str(pi_c)) - 1
    pi_c = decimal.Decimal(pi_c)
    pi_c = pi_c.scaleb(-len_c)
    return pi_c
