import heapq

N = int(input())
M = int(input())

city = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    city[a].append((b, c))  # 도착 도시 b, Cost c

start, end = map(int, input().split())


def dijkstra(start):
    distance = [1e9] * (N+1)
    distance[start] = 0

    heap = [(0, start)]     # cost, 지역 순

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_node, next_cost in city[now]:
            new_cost = dist + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance

result = dijkstra(start)
print(result[end])
