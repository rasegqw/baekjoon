N = int(input())

people = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    count = 0
    for j in range(N):
        if dp[j] == 0:
            if count == people[i]:
                dp[j] = i+1
                break
            count += 1
                
            
for _ in range(N):
    print(dp[_], end=' ')