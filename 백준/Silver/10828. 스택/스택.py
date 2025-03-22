N = int(input())

stack = []

for i in range(N):
    a = input()
    if a.find('push') != -1:
        stack.append(a.split()[1])
    elif a.find('top') != -1:
        if len(stack) > 0:        
            print(stack[-1])
        else:
            print(-1)
    elif a.find('size') != -1:  
        print(len(stack))
    elif a.find('empty') != -1:
        if len(stack)>0:
            print(0)
        else:
            print(1)
    else:             # pop
        if len(stack) > 0:
            print(stack.pop())         
        else:
            print(-1)