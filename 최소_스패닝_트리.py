import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

V, E = map(int, input().split())

parent = [i for i in range(V + 1)]

edges = []
index = 2

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

total = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost

print(total)
