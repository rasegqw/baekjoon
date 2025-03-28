import sys
input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))


start = 0
end = N-1

ans = float('inf')
rkqt = ()

while start < end:

    result = liquid[end] + liquid[start]

    if abs(result) <= ans:
        rkqt = (liquid[start], liquid[end])
        ans = abs(result)

    if result > 0:
        end -= 1
    elif result<0:
        start +=1
    else:
        break


print(rkqt[0], rkqt[1])