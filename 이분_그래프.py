K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V+1)]

    DFS_stack = [1]
    visited = set()
    color = [-1] * (V+1)

    for i in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    color[1] = 0

    while DFS_stack:
        node = DFS_stack.pop()
        if node not in visited:
            visited.add(node)
            for n in reversed(nodes[node]):
                if color[node] == 1:
                    if color[n] == 1:
                        print('NO')
                        DFS_stack = []
                        break
                    color[n] = 0

                else:
                    if color[n] == 0:
                        print('NO')
                        DFS_stack = []
                        break
                    color[n] = 1
                
                DFS_stack.append(n)

        else:
            print('YES')
            continue

            


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
