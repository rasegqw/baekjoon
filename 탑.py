import sys

N = int(input())

stack = list(map(int, sys.stdin.readline().strip().split()))

ans = ['0'] * N

# 내꺼
# start = N - 1

# while start != 0:
#     a = stack.pop()

#     for i in range(len(stack) - 1, -1, -1):
#         if stack[i] > a:
#             ans[start] = str(i + 1)
#             break

#     start -= 1

# A = ' '.join(ans) 

# print(A)


# gpt
index_stack = []

for i in range(N - 1, -1, -1):
    while index_stack and stack[i] >= stack[index_stack[-1]]:
        index_stack.pop()
    
    if index_stack:
        ans[i] = str(index_stack[-1] + 1)  # 1-based index

    index_stack.append(i)

print(' '.join(ans))
