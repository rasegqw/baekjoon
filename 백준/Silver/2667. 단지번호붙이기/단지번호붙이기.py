from collections import deque

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        for i in range(N**2):
            if parents[i] == root_b:
                parents[i] = root_a


N = int(input())

parents = [ i for i in range(N**2)]
board = [[] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().strip()))
    board[i] = a

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

que = deque([[0, 0]])     # y, x

visited = [[False for _ in range(N)] for j in range(N)]

if board[0][0] == 0:
    parents[0] = -1

while que:
    y, x = que.popleft()

    if visited[y][x]:
        continue
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N and 0 <= ny < N) and not visited[ny][nx]:
            if board[ny][nx] == 0:
                parents[ny*N + nx] = -1
            elif board[y][x] == board[ny][nx]:
                union(y*N + x, ny*N + nx)

            que.append([ny, nx])

res = set(parents)
num = 0
ans = []
for i in res:
    if i == -1:
        continue
    count = 0
    for j in parents:
        if j == i:
            count += 1
    ans.append(count)
    num += 1
    
print(num)
ans.sort()
for i in ans:
    print(i)