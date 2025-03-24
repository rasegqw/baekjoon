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
                # 올바르지 않은 괄호
                print(0)
                exit()
        else:
            # 괄호가 닫히지 않은 경우
            print(0)
            exit()

        # result = 0
        
        # if not stack:
        #     break
        # if stack[-1] == '(' :
        #     stack.pop()
        #     stack.append(2)
        # elif type(stack[-1]) == int :
        #     while stack and type(stack[-1]) == int :
        #         result += stack.pop()


        #     if not stack or stack[-1] != '(':
        #         stack = []
        #         break
        #     if stack[-1] == '(':
        #         stack.pop()
        #         stack.append(result * 2)

        # else:
        #     stack = []
        #     break
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


        # result = 0
        
        # if not stack:
        #     break
        # if stack[-1] =='[' :
        #     stack.pop()
        #     stack.append(3)
        # elif type(stack[-1]) == int :
        #     while stack and type(stack[-1]) == int :
        #         result += stack.pop()
                
        #     if not stack or stack[-1] != '[':
        #         stack = []
        #         break                
        #     if stack[-1] == '[':
        #         stack.pop()
        #         stack.append(result * 3)
        # else:
        #     stack = []
        #     break
for i in stack:
    if not isinstance(i, int):
        print(0)
        exit()
        
print(sum(stack))

