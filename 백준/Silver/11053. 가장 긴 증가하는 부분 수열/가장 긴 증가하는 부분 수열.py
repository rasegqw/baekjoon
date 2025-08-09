import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

res = 0
dp = [nums[0]]

for num in nums[1:]:
    for i in range(len(dp)):
        if num <= dp[i]:
            dp[i] = num
            break
    if i == len(dp) - 1 and dp[i] != num:
        dp.append(num)

print(len(dp))