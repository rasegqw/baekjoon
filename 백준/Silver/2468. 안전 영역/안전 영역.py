import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in board)
max_cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, h, visited):
    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n: 
                if board[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
for h in range(max_height):
    visited = [[False] * n for _ in range(n)]
    safe_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and board[i][j] > h:
                bfs(i, j, h, visited)
                safe_cnt += 1
    max_cnt = max(max_cnt, safe_cnt)

print(max_cnt)