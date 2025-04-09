N, M = map(int, input().split())

parents= [i for i in range(N+1)]

def find(x):
    if parents[x] != x:
        x = find(parents[x])
    return x

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        for i in range(1, N+1):
            if parents[i] == root_b:
                parents[i] = root_a

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

res = set(parents)

print(len(res)-1)