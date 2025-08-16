import sys

input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))

foods = [ list(map(int, input().split())) for _ in range(N) ]

res = []
min_price = 1 << 13

for mask in range(1, 1<<N):
    total = [0, 0, 0, 0, 0]
    x = []
    for i in range(N):
        if mask & (1<<i):
            total[0] += foods[i][0]
            total[1] += foods[i][1]
            total[2] += foods[i][2]
            total[3] += foods[i][3]
            total[4] += foods[i][4]
    if total[0] >= target[0] and total[1] >= target[1] and total[2] >= target[2] and total[3] >= target[3]:
        if min_price > total[4]:
            min_price = total[4]
            res = [j+1 for j in range(N) if mask & (1<<j)]
        elif min_price == total[4]:
            x = [j+1 for j in range(N) if mask & (1<<j)]
            if res > x:
                res = x
if min_price == 1<<13:
    print(-1)
else:
    print(min_price)
    print(*res)