import sys

input = sys.stdin.readline

N, target = map(int, input().split())

nums = list(map(int, input().split()))

bit = 1
cnt = 0

while bit < 1<<N:
    sum = 0
    for i in range(N):
        if bit & (1<<i):
            sum += nums[i]

    if sum == target:
        cnt += 1
    bit += 1

print(cnt)