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

            
    # 힙큐는 항상 min heap을 디폴트로 갖기 때문에 최대 힙에 대해선
    # 조심