# import sys

# N = int(input())

# Nums = list(map(int, sys.stdin.readline().split()))
# minus = []
# plus = []
# zero_count = 0

# for i in Nums:
#     if i < 0:
#         minus.append(i)
#     elif i>0:
#         plus.append(i)
#     else:
#         zero_count += 1

# if zero_count > 1:
#     print('0 0')


# else:
#     plus.sort()
#     minus.sort(key=abs)
#     posi = 0
#     nega = 0
    
#     if zero_count == 1:
#         zero_ans = min(plus[0], abs(minus[0]))
    
#     while posi<len(plus) and nega<len(minus) :

#         result = plus[posi] + minus[nega]

#         if posi==0 and nega ==0:
#             ans = [posi, nega]
#             pre_res = plus[posi] + minus[nega]

#         if abs(result) < abs(pre_res):
#             ans = [posi, nega]
#             pre_res = result

#         if result == 0:
#             break
#         elif result > 0:
#             nega += 1
#         elif result < 0:
#             posi += 1

#     if zero_count == 1 and zero_ans < result :
#         if abs(minus[0]) < plus[0]:
#             print(f'{minus[0]} 0')
#         else:
#             print(f'0 {plus[0]}')
#     else:
#         print(f'{minus[ans[1]]} {plus[ans[0]]}')

import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

left = 0
right = N - 1
min_sum = float('inf')
answer = (0, 0)

while left < right:
    total = nums[left] + nums[right]

    if abs(total) < min_sum:
        min_sum = abs(total)
        answer = (nums[left], nums[right])

    if total < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
