# import math

# N, B = map(int, input().split())

# A = [0] * N

# n = int(math.log2(B))

# for i in range(N):
#     a = list(map(int, input().split()))
#     for j in range(len(a)):
#         a[j] %=1000
#     A[i] = a

# # 계속 제곱해가면서 해당 행렬 저장하고, B에 맞춰가는 식으로 해보자.
# res = []
# ans = []
# ans.append(A)

# if B == 1:
#     for i in range(N):
#         print(*ans[-1][i])
#     exit()

# while n>len(ans)-1 :
#     res = []
#     for i in range(N):
#         a = []
#         for k in range(N):
#             total = 0
#             for j in range(N):
#                 total += ans[-1][i][j] * ans[-1][j][k]
#             if total >= 1000:
#                 total %= 1000
#             a.append(total)
#         res.append(a)
#     ans.append(res)

# x = B-2**n
# needone = []
# for i in range(n):
#     if x >= 2**(n-i):
#         x -= 2**(n-i)
#         needone.append(n-i)
#     elif x == 0:
#         break
#     elif x == 1:
#         needone.append(0)
#         break
        
# for y in needone :
#     res = []
#     for i in range(N):
#         a = []
#         for k in range(N):
#             total = 0
#             for j in range(N):
#                 total += ans[-1][i][j] * ans[y][j][k]
#             if total >= 1000:
#                 total %= 1000
#             a.append(total)
#         res.append(a)
#     ans.append(res)

# for i in range(N):
#     print(*ans[-1][i])





# def forB(arr, b):
#     res = []

#     b -1

#     for i in range(N):
#         a = []
#         for k in range(N):
#             total = 0
#             for j in range(N):
#                 total += A[i][j] * A[j][k]
#             a.append(total)
#         res.append(a)



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
