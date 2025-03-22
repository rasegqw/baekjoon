from collections import deque

N = int(input())

stack = []

# find 함수는 해당 값을 찾으면, 인덱스를 불러옴
# 못찾으면 -1 불러옴
for i in range(N):
    a = input()
    if a.find('push') != -1:
        stack.append(a.split()[1])
    elif a == 'top' :
        if len(stack) > 0:        
            print(stack[-1])
        else:
            print(-1)
    elif a == 'size' :  
        print(len(stack))
    elif a == 'empty' :
        if len(stack)>0:
            print(0)
        else:
            print(1)
    else:             # pop
        if len(stack) > 0:
            print(stack.pop())         
        else:
            print(-1)