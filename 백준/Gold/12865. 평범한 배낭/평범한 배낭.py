N, K = map(int, input().split())

items = []

for i in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

dp = [[0 for _ in range(N+1)] for __ in range(K+1)]

j = 1
for weight, value in items:
    for i in range(1, K+1):
        if i-weight < 0:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-weight][j-1] + value)
    j += 1

print(dp[K][N])
