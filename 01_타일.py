N = int(input())
dp = [0 for _ in range(N+1)]


if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    print(dp[-1])

# N = int(input())

# prev1 = 1
# prev2 = 2
# if N == 1:
#     print(prev1)
# elif N == 2:
#     print(prev2)
# else:
#     for i in range(N-2):
#         prev1, prev2 = prev2, prev1 + prev2

#     print(prev2)

# def matrix_mul(A, B):
#     return [
#         [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
#         [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
#     ]

# def matrix_pow(mat, power):
#     result = [[1, 0], [0, 1]]  # 단위 행렬
#     while power:
#         if power % 2 == 1:
#             result = matrix_mul(result, mat)
#         mat = matrix_mul(mat, mat)
#         power //= 2
#     return result

# def fast_fib(n):
#     if n == 1:
#         return 1
#     base = [[1, 1], [1, 0]]
#     res = matrix_pow(base, n - 1)
#     return res[0][0]

# N = int(input())
# if N == 1:
#     print(1)
# elif N == 2:
#     print(2)
# else:
#     print(fast_fib(N+1)%15746)
