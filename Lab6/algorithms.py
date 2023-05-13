import decimal
from math import *
from decimal import Decimal, getcontext
import math
import mpmath
import sys
import math

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


def machin_pi():
    mpmath.mp.dps = 50000
    pi = 4 * (4 * mpmath.atan(1 / 5) - mpmath.atan(1 / 239))
    return pi


def sqrtPI(n, m):
    m1 = 10 ** 16
    m2 = float((n * m1) // m) / m1
    b = (int(m1 * math.sqrt(m2)) * m) // m1
    n_m = n * m
    while True:
        a = b
        b = (b + n_m // b) // 2
        if b == a:
            break
    return b


def power(n):
    if n == 0:
        return 1
    r = power(n // 2)
    if n % 2 == 0:
        return r * r
    return r * r * 10


# Chudnovsky algorithm

def chudnovsky_pi():
    mpmath.mp.dps = 100000
    m = power(100000)
    c = (640320 ** 3) // 24
    n = 1
    Ak = m
    Asum = m
    Bsum = 0
    while Ak != 0:
        Ak *= -(6 * n - 5) * (2 * n - 1) * (6 * n - 1)
        Ak //= n * n * n * c
        Asum += Ak
        Bsum += n * Ak
        n = n + 1
        result = (426880 * sqrtPI(10005 * m, m) * m) // (13591409 * Asum + 545140134 * Bsum)
        return result
