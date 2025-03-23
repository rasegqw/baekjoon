N = input()
stack = []

for i in N:
    if i == '(' or i == '[':
        stack.append(i)

    elif i == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if tmp == 0 else 2 * tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                # 올바르지 않은 괄호
                print(0)
                exit()
        else:
            # 괄호가 닫히지 않은 경우
            print(0)
            exit()

    elif i == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if tmp == 0 else 3 * tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

# 최종 스택 검사: 숫자만 남아있어야 함
for s in stack:
    if not isinstance(s, int):
        print(0)
        exit()

print(sum(stack))
