import sys
from bisect import bisect_left, bisect_right

M, N, L = map(int, sys.stdin.readline().split())

Mnums = list(map(int, sys.stdin.readline().split()))
Mnums.sort()

count = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if y > L:
        continue

    # bisect로 위치 찾기
    a = bisect_left(Mnums, x) - 1
    b = bisect_left(Mnums, x)

    # 거리 계산
    valid = False

    # a가 유효하면 거리 계산
    if a >= 0 and abs(Mnums[a] - x) <= L - y:
        valid = True

    # b가 유효하면 거리 계산
    if b < M and abs(Mnums[b] - x) <= L - y:
        valid = True

    if valid:
        count += 1

print(count)