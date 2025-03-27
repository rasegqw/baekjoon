import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

Have_num = list(map(int, input().strip().split()))
Have_num.sort()

M = int(input())

isGot = list(map(int, input().strip().split()))
ans = [None] * M

for i in range(M):
    a = bisect_left(Have_num, isGot[i])
    if a > N-1:
        ans[i] = 0
        continue
    if isGot[i] == Have_num[a]:
        ans[i] = 1
    else:
        ans[i] = 0
for i in range(M):
    print(ans[i], end= ' ')
            