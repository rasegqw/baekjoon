def matrix_mul(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def matrix_pow(mat, power):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while power:
        if power % 2 == 1:
            result = matrix_mul(result, mat)
        mat = matrix_mul(mat, mat)
        power //= 2
    return result

def fast_fib(n):
    if n == 1:
        return 1
    base = [[1, 1], [1, 0]]
    res = matrix_pow(base, n - 1)
    return res[0][0]

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    print(fast_fib(N+1)%15746)