N, M =map(int, input().split())

parent = [i for i in range(N+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        for i in range(N+1):
            if parent[i] == root_y:
                parent[i] = root_x



for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)


parent = set(parent)


print(len(parent)-1)