from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

tree = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (N + 1)  
queue = deque([1])  
visited = set([1])  

while queue:
    node = queue.popleft()
    for child in tree[node]:  # 현재 노드의 연결된 노드들 탐색
        if child not in visited:  # 방문하지 않은 노드만 처리
            parent[child] = node  # 현재 노드가 자식 노드의 부모가 됨
            visited.add(child)
            queue.append(child)

for i in range(2, N + 1):
    print(parent[i])