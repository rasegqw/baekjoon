def matrix_mul(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

def matrix_power(A, B, N):
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)] # 단위 행렬
    while B > 0:
        if B % 2 == 1:
            result = matrix_mul(result, A, N)
        A = matrix_mul(A, A, N)
        B //= 2
    return result

N, B = map(int, input().split())

A = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]

result = matrix_power(A, B, N)

for row in result:
    print(*row)
