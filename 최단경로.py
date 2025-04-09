import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

start = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited = [False] * (V+1)
distance = [1e9] * (V+1)

distance[start] = 0
heap = [[0, start]]

while heap:
    cost, now = heapq.heappop(heap)    
    visited[now] = True

    if distance[now] < cost:  # 이미 처리된 노드면 스킵
        continue

    for next_node, weight in graph[now]:
        cs = cost + weight
        if cs < distance[next_node]:  # 더 짧은 거리 발견
            distance[next_node] = cs
            heapq.heappush(heap, (cs, next_node))

for i in distance[1:]:
    if i == 1e9:
        print('INF')
    else:
        print(i)
