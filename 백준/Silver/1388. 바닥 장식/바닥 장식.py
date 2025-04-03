from collections import deque

N, M = map(int, input().split())

board = [[] for _ in range(N)]
parents = [ i for i in range(N*M)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parents[b] = root_a

for i in range(N):
    a = list(map(str, input().strip()))
    board[i] = a

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

que = deque([[0,0]])

visited = [[False for _ in range(M)] for j in range(N)]

while que:
    y, x = que.popleft()

    if visited[y][x]:
        continue
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            
            if (i == 0 or i == 1) and board[y][x] == board[ny][nx] == '-':
                union(y*M + x, ny*M + nx)
            elif (i == 2 or i == 3) and board[y][x] == board[ny][nx] == '|':
                union(y*M + x, ny*M + nx)

            que.append([ny, nx])

res = set(parents)
print(len(res))