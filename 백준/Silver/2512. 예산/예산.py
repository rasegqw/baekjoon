import sys
input = sys.stdin.readline

N = int(input())

required_money = list(map(int, input().split()))

money = int(input())

start = 1
end = max(required_money)


while start <= end:
    mid = (start + end)//2
    total = 0
    for i in required_money:
        if i <= mid:
            total += i
        else:
            total += mid

    if total > money :
        end = mid - 1
    else:
        start = mid + 1

print(min(start, end))