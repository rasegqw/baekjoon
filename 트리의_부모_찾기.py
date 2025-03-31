from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

Nodes = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().strip().split())

    Nodes[a].append(b)
    Nodes[b].append(a)

visited = set()
parents = [i for i in range(N+1)]
que = deque([1])

while que:
    x = que.popleft()

    for i in Nodes[x]:
        if i in visited:
            continue
        parents[i] = x
        que.append(i)

    visited.add(x)

for i in range(2, N+1):
    print(parents[i])

# from collections import deque
# import sys

# input = sys.stdin.readline

# N = int(input())

# tree = {i: [] for i in range(1, N + 1)}

# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# parent = [0] * (N + 1)  
# queue = deque([1])  
# visited = set([1])  

# while queue:
#     node = queue.popleft()
#     for child in tree[node]:  # 현재 노드의 연결된 노드들 탐색
#         if child not in visited:  # 방문하지 않은 노드만 처리
#             parent[child] = node  # 현재 노드가 자식 노드의 부모가 됨
#             visited.add(child)
#             queue.append(child)

# for i in range(2, N + 1):
#     print(parent[i])