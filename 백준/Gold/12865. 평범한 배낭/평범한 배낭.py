N, K = map(int, input().split())

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [0] * (K + 1)

for weight, value in items:
    for i in range(K, weight - 1, -1): 
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[K])
