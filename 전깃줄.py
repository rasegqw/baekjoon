N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

lines.sort(key=lambda x: x[0])

B = [b for a, b in lines]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
