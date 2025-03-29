from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite(V, nodes):
    color = [-1] * (V + 1)

    for start in range(1, V + 1):
        if color[start] == -1:  # 방문하지 않은 컴포넌트
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()
                for neighbor in nodes[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # 다른 색으로 칠하기
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # 같은 색 이웃 발견 → 이분 그래프 아님

    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    if is_bipartite(V, nodes):
        print("YES")
    else:
        print("NO")