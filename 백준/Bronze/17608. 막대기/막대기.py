import sys

N = int(input())

stack = [None] * N
DP = [1] * N

for i in range(N):
    stack[i] = int(sys.stdin.readline())

pivot_num = stack[-1]

for i in range(N-2, -1, -1):
    if stack[i] > pivot_num:
        DP[i] = DP[i+1] + 1
        pivot_num = stack[i]
    else:
        DP[i] = DP[i+1]

print(DP[0])