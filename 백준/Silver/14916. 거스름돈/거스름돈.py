n = int(input())

dp = [0] * (n+1)


if n == 1 or n == 3:
    print(-1)
    exit()
elif n == 2 or n == 5:
    print(1)
    exit()
elif n == 4:
    print(2)
    exit()

dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    
    if dp[i-2] == 0:
        if dp[i-5] == 0:
            continue
        dp[i] = dp[i-5]+1

    elif dp[i-5] == 0:
        dp[i] = dp[i-2]+1    
    
    else:
        dp[i] = min(dp[i-2]+1, dp[i-5]+1)

print(dp[-1] if dp[-1] != 0 else -1)