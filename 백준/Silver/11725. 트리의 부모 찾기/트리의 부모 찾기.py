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