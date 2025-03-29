# from collections import deque

# N, M = map(int, input().split())

# bing_san = [list(map(int, input().split())) for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# not_sea = []
# min_height = 11

# for i in range(N):
#     for j in range(M):
#         if bing_san[i][j] != 0 :
#             min_height = min(bing_san[i][j], min_height)
#             not_sea.append((i, j))  # y, x


# while True:


#     min_height += 1

# for i in range(4):

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def melt():
    melt_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                water = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < m:
                        if graph[ni][nj] == 0:
                            water += 1
                melt_list.append((i, j, water))

    for i, j, water in melt_list:
        graph[i][j] = max(graph[i][j] - water, 0)

year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1

    if count == 0:
        print(0)
        break
    if count >= 2:
        print(year)
        break

    melt()
    year += 1
