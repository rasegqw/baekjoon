N = input()

stack = []
result = 0


for i in N:
    if i == '(':
        stack.append('(')

    elif i ==')':

        result = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if result == 0 else 2 * result)
                break
            elif isinstance(top, int):
                result += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()


    elif i=='[':
        stack.append('[')

    else:
        result = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if result == 0 else 3 * result)
                break
            elif isinstance(top, int):
                result += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

for i in stack:
    if not isinstance(i, int):
        print(0)
        exit()
        
print(sum(stack))
