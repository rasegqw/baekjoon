import sys

input = sys.stdin.readline

n = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

left, right = 0, n-1

res = []
abs_add_two = 1 << 30

if liquids[-1] <= 0:
    print(liquids[-2], liquids[-1])
elif liquids[0] >= 0:
    print(liquids[0], liquids[1])
else:
    while left < right:
        result = liquids[left] + liquids[right]

        if abs(result) < abs_add_two:
            res = [liquids[left], liquids[right]]
            abs_add_two = abs(result)
        
        if result > 0:
            right -= 1
        elif result < 0:
            left += 1
        else:
            break

    print(res[0], res[1])