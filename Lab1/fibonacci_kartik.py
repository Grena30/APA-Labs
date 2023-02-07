
def fibonacci_kartik(n):
    if n > 0:
        n1, n2 = 1, 1
        if n > 3:
            for _ in range((n // 3)):
                n1, n2 = n2, (n2 << 2) + n1  # << 2   is multiply by 4
        if n % 3 == 0:
            return n1
        elif n % 3 == 1:
            return (n2 - n1) >> 1  # >> 1   is divide by 2  'F1'
        elif n % 3 == 2:
            return (n2 + n1) >> 1  # >> 1   is divide by 2  'F2'
    else:
        return -1
