import sys
import heapq

# 입력 처리
input = sys.stdin.read
data = input().strip().split("\n")

N = int(data[0])  # 첫 번째 줄: N

# 그래프 및 진입 차수 배열 초기화
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

# 인접 행렬 입력 받아 그래프 구성
for i in range(1, N + 1):
    row = list(map(int, data[i]))  # 한 줄을 정수 리스트로 변환
    for j in range(1, N + 1):
        if row[j - 1] == 1:  # i → j 간선 존재 (0-based index)
            graph[j].append(i)  # **정점 방향 반대로 저장**
            in_degree[i] += 1  # 진입 차수 증가

# 위상 정렬을 위한 우선순위 큐 (작은 숫자부터)
pq = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, -i)  # 큰 숫자부터 나오도록 음수 저장

result = [0] * (N + 1)
order = N  # **가장 큰 순서부터 배정**
count = 0  # 방문한 노드 수

while pq:
    node = -heapq.heappop(pq)  # 가장 큰 번호부터 선택
    result[node] = order
    order -= 1
    count += 1  # 방문한 노드 수 증가

    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(pq, -neighbor)  # 큰 숫자가 먼저 나오도록 처리

# 사이클이 있는 경우 (-1 출력)
if count < N:
    print(-1)
else:
    print(" ".join(map(str, result[1:])))
