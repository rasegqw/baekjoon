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
