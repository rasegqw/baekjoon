MOD = 1000000000

N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(K + 1):
    dp[i][0] = 1  # 0을 만드는 방법은 항상 1가지 (모두 0)

for k in range(1, K + 1):
    for n in range(1, N + 1):
        dp[k][n] = (dp[k][n - 1] + dp[k - 1][n]) % MOD

print(dp[K][N])
