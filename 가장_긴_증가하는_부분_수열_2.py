import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
Anums = list(map(int, input().split()))

stack = [Anums[0]]

# for i in Anums[1:]:
#     a = bisect_left(stack, i)

#     if i > stack[a] and len(stack) == a+1:
#         stack.append(i)

#     elif i 




#         # if i <= stack[j]:
#         #     stack[j] = i
#         #     break
#         # else:
#         #     if j == len(stack)-1:
#         #         stack.append(i)
#         #     continue    


# print(len(stack))

for num in Anums:
    idx = bisect_left(stack, num)
    if idx == len(stack):
        stack.append(num)
    else:
        stack[idx] = num

print(len(stack))