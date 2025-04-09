T = int(input())

for _ in range(T):
    N = int(input())

    coins = list(map(int, input().split()))

    M = int(input())
    
    dp = [0] * (M + 1)
    dp[0] = 1  # 금액 0을 만드는 방법은 아무 동전도 사용하지 않는 1가지
    
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
    
    print(dp[M])