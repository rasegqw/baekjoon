# N = int(input())

# matrixs = []

# for i in range(N):
#     a, b = map(int, input().split())
#     matrixs.append([a, b])

# if N == 1:
#     print(matrixs[0][0] * matrixs[0][1])

# elif N == 2:
#     result = matrixs[0][0] * matrixs[0][1] * matrixs[1][1]
#     print(result)

# else:
#     dp = [0] * (N+1)
#     dp[1] = matrixs[0][0] * matrixs[0][1]
#     dp[2] = dp[1] * matrixs[1][1]

#     for i in range(3, N+1):
#         dp[i] = min(dp[i-1] + matrixs[0][0] * matrixs[i-2][1] * matrixs[i-1][1], matrixs[i-2][0] * matrixs[i-2][1] * matrixs[i-1][1] + dp[i-2] * matrixs[i-1][1])
        
#     print(dp[-1])

import sys
input = sys.stdin.readline

N = int(input())
dim = []
for _ in range(N):
    r, c = map(int, input().split())
    dim.append((r, c))

dp = [[0]*N for _ in range(N)]

for length in range(1, N):  
    for i in range(N - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + dim[i][0] * dim[k][1] * dim[j][1]
            if cost < dp[i][j]:  
                dp[i][j] = cost

print(dp[0][N-1])


# import sys
# input = sys.stdin.readline
# INF = sys.maxsize

# def solution(N: int, mat: list):
#     arr = [i[0] for i in mat] + [mat[-1][1]]
#     dp = [[0] * (N + 1) for _ in range(N + 1)]
    
#     for j in range(1, N + 1):
#         for i in range(j - 1, 0, -1):
#             temp = INF
#             for k in range(i, j):
#                 if temp > dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]:
#                     temp = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
#             dp[i][j] = temp
    
#     print(dp[1][-1])

# N = int(input())
# mat = [list(map(int, input().split())) for _ in range(N)]
# solution(N, mat)