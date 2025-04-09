import sys
import heapq
input = sys.stdin.readline

INF = 1e6

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

v1, v2 = map(int, input().split())

distance = [[INF, []] for _ in range(N+1)]
visited = [False] * (N+1)

distance[1] = (0, [1])
heap = [(distance[1], 1)]

while heap:
    cost_path, now = heapq.heappop(heap)

    if visited[now] == True:
        continue

    visited[now] = True

    for next, next_cost in graph[now]:
        if next == N and (v1 or v2) not in distance[now][1]:
            continue
        if distance[next][0] > (cost_path[0] + next_cost) and visited[next] == False:
            distance[next][1].extend(cost_path[1])
            distance[next][1].append(next)
            distance[next][0] = cost_path[0] + next_cost
            heapq.heappush(heap, (distance[next], next))

print(distance[-1][0])