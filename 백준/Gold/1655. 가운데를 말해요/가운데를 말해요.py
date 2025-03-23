import heapq
import sys

N = int(input())
upper_mid = []
under_mid = []
under_mid.append(-int(sys.stdin.readline()))
print(-under_mid[0])

if N == 1:
    exit()

else:
    for i in range(1, N):
        num = int(sys.stdin.readline())
        if num <= -under_mid[0]:
            heapq.heappush(under_mid, -num)
        else:
            heapq.heappush(upper_mid, num)

        if len(upper_mid) > len(under_mid) :
            heapq.heappush(under_mid, -heapq.heappop(upper_mid))
        elif len(under_mid) - len(upper_mid) > 1 :
            heapq.heappush(upper_mid, -heapq.heappop(under_mid))

        print(-under_mid[0])