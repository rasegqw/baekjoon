from collections import deque

N, M, V = map(int, input().split())

nodes = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i in range(1, N+1):
    if nodes[i]:
        nodes[i].sort()



def BFS(start):
    global nodes
    
    cur = deque([start])
    result = []
    while cur:
        current = cur.popleft()
        if current not in result:
            result.append(current)
            
        for n in nodes[current]:
            if n not in result:
                cur.append(n)
    return result

def DFS(start):
    global nodes

    stack = [start]
    visited = set()
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            for n in reversed(nodes[node]):
                stack.append(n)

    return result

print(*DFS(V))
print(*BFS(V))