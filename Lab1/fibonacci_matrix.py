
def fibonacci_matrix(n):
    if n == 0:
        return 0
    else:
        A = [[1, 1], [1, 0]]
        power(A, n - 1)
        return A[0][0]


def power(A, n):
    M = [[1, 1],
         [1, 0]]

    for i in range(2, n + 1):
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

