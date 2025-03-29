import sys
# import heapq
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

types = [int(input()) for _ in range(n)]

# heap = [(0, 0)]     # count , total
que = deque([(0,0)])
visited = [False] * (k + 1)


min_count = 10001
# while heap :
while que:
    # (count, total) = heapq.heappop(heap)
    count, total = que.popleft()

    if total == k:
        min_count = min(min_count, count)

    if total > k or count > min_count:
        continue

    for i in types:
        a = total + i
        # if (count, a) in heap:
        if a <= k and not visited[a]:            
            visited[a] = True
            que.append((count+1, a))
        # heapq.heappush(heap, (count, a))


print(-1 if min_count == 10001 else min_count)