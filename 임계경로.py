# from collections import deque

# N = int(input())

# M = int(input())

# graph = [[] for _ in range(N)]
# for _ in range(M):
#     u, v, w = map(int, input().split())

#     graph[u].append([v, w])

# start, end = map(int, input().split())

# que = deque([[0, start, 0]])    # dist, start, count
# result = []

# while que:
#     dist, now, count = que.pop()


#     if now == end:
#         result.append([dist, count])

#     for dest, cost in graph[now]:
#         que.append([dist + cost, dest, count + 1])


# for i, j in result:

# print(max(result), )


import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N = int(input())  # 도시 개수
M = int(input())  # 도로 개수

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
time = [0] * (N + 1)  # 최장 거리 저장

# 그래프 입력 받기
for _ in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))  # 정방향 그래프
    reverse_graph[B].append((A, cost))  # 역방향 그래프
    in_degree[B] += 1  # 진입 차수 증가

# 출발점과 도착점 입력 받기
start, end = map(int, input().split())

# 1️⃣ 위상 정렬을 활용한 "최장 경로 찾기"
queue = deque()
queue.append(start)

while queue:
    now = queue.popleft()
    
    for next_node, cost in graph[now]:
        # 최장 거리 갱신
        if time[next_node] < time[now] + cost:
            time[next_node] = time[now] + cost
        
        # 진입 차수 감소 후 0이면 큐에 추가
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

# 도착점에서 최장 경로 시간 출력
max_time = time[end]

# 2️⃣ 역방향 그래프를 이용한 "필수 도로 개수 찾기"
queue = deque()
queue.append(end)
visited = [False] * (N + 1)
critical_path_count = 0

while queue:
    now = queue.popleft()
    
    for prev_node, cost in reverse_graph[now]:
        # "필수 도로"인지 확인 (최장 경로에 사용된 간선)
        if time[now] == time[prev_node] + cost:
            critical_path_count += 1
            if not visited[prev_node]:  # 중복 방문 방지
                queue.append(prev_node)
                visited[prev_node] = True

# 결과 출력
print(max_time)
print(critical_path_count)
