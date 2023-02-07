from decimal import Decimal


def fibonacci_binet(n):
    phi = (1 + Decimal(5).sqrt()) / 2
    psi = (1 - Decimal(5).sqrt()) / 2
    return int((pow(phi, n) - pow(psi, n)) / Decimal(5).sqrt())
