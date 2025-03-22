import heapq
import sys

N = int(input())

Heap = []

for i in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(Heap, -a)
    else:
        if len(Heap) != 0:
            print(-heapq.heappop(Heap))
        else:
            print(0)