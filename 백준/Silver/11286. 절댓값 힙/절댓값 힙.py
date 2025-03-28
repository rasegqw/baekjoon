import sys
import heapq
input = sys.stdin.readline

N = int(input())

H = []
for i in range(N):
    a = int(input())

    if a == 0:
        if H:
            print(heapq.heappop(H)[1])
        else:
            print(0)
    else:
        heapq.heappush(H, (abs(a), a))
