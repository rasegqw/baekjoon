first = list(map(str, input().strip()))
sec = list(map(str, input().strip()))

dp = [[0 for _ in range(len(sec) + 1)] for __ in range(len(first) + 1)]

for i in range(1, len(first)+1):
    for j in range(1, len(sec)+1):
        if first[i-1] == sec[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(first)][len(sec)])