import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

stack = []
stack.append(A[-1])

ans = [-1]
i = N-2
while i != -1:
    while stack and (stack[-1] <= A[i]):
        stack.pop()

    if not stack:
        ans.append(-1)
        stack.append(A[i])
    else:    
        a = stack[-1]

        ans.append(a)
        stack.append(A[i])

    i -= 1

for i in ans[::-1]:
    print(i, end=' ')