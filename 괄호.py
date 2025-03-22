import sys
N = int(input())

for i in range(N):
    stack = []
    a = sys.stdin.readline().strip()
    
    for j in a:
        if j == '(':
            stack.append(True)
        else:
            if len(stack) == 0:
                stack.append(False)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')       