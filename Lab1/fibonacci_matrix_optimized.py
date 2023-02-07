def fibonacci_matrix_op(n):
    if n == 0:
        return 0
    else:
        A = [[1, 1], [1, 0]]
        power(A, n - 1)
        return A[0][0]


# Optimized power method

def power(A, n):
    if n == 0 or n == 1:
        return

    M = [[1, 1],
         [1, 0]]

    power(A, n // 2)
    matrixMultiplication(A, A)

    if n % 2 != 0:
        matrixMultiplication(A, M)


def matrixMultiplication(A, B):
    a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    b = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    d = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    A[0][0] = a
    A[0][1] = b
    A[1][0] = c
    A[1][1] = d
