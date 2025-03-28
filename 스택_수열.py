import sys
input = sys.stdin.readline

N = int(input())
stack = []
x = 0
ans = []
for i in range(N):
    a = int(input())

    if a<x:
        if a == stack[-1]:
            stack.pop()
            ans.append('-')
        else:
            print('NO')
            exit()
    else:
        for i in range(x, a):
            ans.append('+')
            stack.append(i+1)

        x = stack.pop()
        ans.append('-')

for i in range(len(ans)):
    print(ans[i])