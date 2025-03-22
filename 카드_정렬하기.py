import heapq
import sys

N = int(input())

H = [None] * N

for i in range(N):
    H[i] = int(sys.stdin.readline())

if N == 1:
    print(H[0])

else:
    heapq.heapify(H)
    first = heapq.heappop(H)
    sec = heapq.heappop(H)
    sum = first + sec
    total = first + sec
    heapq.heappush(H, total)
    count = N - 2
    while count != 0:  
        total = heapq.heappop(H)+heapq.heappop(H)  
        heapq.heappush(H, total)
        sum += total
        count -= 1

    print(sum)