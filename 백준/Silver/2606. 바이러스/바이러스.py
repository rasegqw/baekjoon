N = int(input())

edge = int(input())

parents = [i for i in range(N+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parents[root_y] = root_x
        for i in range(N+1):
            if parents[i] == root_y:
                parents[i] = root_x



for i in range(edge):
    a, b = map(int, input().split())
    union(a, b)

count = 0
for i in range(2, N+1):
    if parents[i] == parents[1]:
        count += 1

print(count)