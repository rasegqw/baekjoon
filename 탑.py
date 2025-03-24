# try 1

# import sys

# N = int(input())

# stack = list(map(int, sys.stdin.readline().strip().split()))


# ans = []
# for i in range(N-1, 0, -1):
#     for j in range(i-1, -1, -1):
#         if stack[j]>stack[i]:
#             ans.append(j+1)
#             break
#         elif j == 0:
#             ans.append(0)

# ans.append(0)

# print(*ans[::-1])



# try 2

# ans = ['0'] * N

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


# try 3

import sys

input = sys.stdin.readline
N = int(input())
top = list(map(int, input().split()))

stack = []  
ans = [0] * N

for i in range(N):
    while stack and stack[-1][1] <= top[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1][0] + 1  
    stack.append((i, top[i]))

print(*ans)




