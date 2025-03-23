import sys

input = sys.stdin.readline
N = int(input())
top = list(map(int, input().split()))

stack = []  
ans = [0] * N

for i in range(N):
    while stack and stack[-1][1] <= top[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1][0] + 1  
    stack.append((i, top[i]))

print(*ans)
