from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

indeg = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indeg[b-1] += 1

que = deque()

for i in range(N):
    if indeg[i] == 0:
        que.append(i)


result = deque()

while que:
    now = que.popleft()
    result.append(now)

    for next in graph[now]:
        indeg[next] -= 1
        if indeg[next] == 0:
            que.append(next)

for i in range(N):
    print(result.popleft()+1,end=' ') 
    