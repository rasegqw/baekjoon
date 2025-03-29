from collections import deque

N, M, K, X = map(int, input().split())

city = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

go_count = [-1] * (N+1)
go_count[X] = 0
cur = deque([X])

while cur:
    current = cur.popleft()
    for i in city[current]:
        if go_count[i] == -1:
            go_count[i] = go_count[current] + 1
            cur.append(i)

result = []

for i in range(1, N+1):
    if go_count[i] ==K:
        result.append(i)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)

    
    