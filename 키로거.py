import sys
input = sys.stdin.readline

N = int(input())

test_case=[]

for i in range(N):
    test_case.append(input().strip())

stack = []
i = 0

for k in test_case:
    for j in k:
        if j =="<":
            i = i - 1 if i !=0 else i
        elif j == '>':
            i = i + 1 if i+1 <= len(stack) else i
        elif j == '-':
            if not stack or i == 0:
                continue
            if i < len(stack) and stack:
                stack.pop(i-1)
                i = i - 1 if i !=0 else i
            else:
                stack.pop()
                i = i - 1 if i !=0 else i
        else:
            if i < len(stack) and stack:
                stack.insert(i,j)
                i += 1
            else:
                stack.append(j)
                i += 1

    print(''.join(stack))
    stack = []
    i = 0