import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
visited = [False] * (N+1)

cnt = 0
max_cnt = 0

for target in nums:
    if visited[target]:
        cnt -= 1
    else:
        visited[target] = True
        cnt += 1
        max_cnt = max(cnt, max_cnt)
        
print(max_cnt)