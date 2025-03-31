import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
a = input().strip()
place = [0] + list(map(int, a))  # 1-based index

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
answer = 0

def dfs(node):
    visited[node] = True
    indoor_count = 0  # 실내 노드 개수 카운트

    for neighbor in graph[node]:
        if place[neighbor] == 1:  # 연결된 실내 노드 찾기
            indoor_count += 1
        elif not visited[neighbor]:  # 실외 노드라면 DFS 계속 탐색
            indoor_count += dfs(neighbor)

    return indoor_count

for i in range(1, N + 1):
    if place[i] == 0 and not visited[i]:  # 실외 노드에서 탐색
        cnt = dfs(i)
        answer += cnt * (cnt - 1)  # 가능한 모든 (i, j) 경우의 수 추가

for i in range(1, N + 1):
    if place[i] == 1:
        for j in graph[i]:
            if place[j] == 1:  # 실내-실내 직접 연결된 경우
                answer += 1  # 중복 방지 X (모든 간선 체크 필요)

print(answer)