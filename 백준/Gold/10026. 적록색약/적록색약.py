
import sys
from collections import deque

# 입력
N = int(sys.stdin.readline().strip())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, color_blind):
    queue = deque([(x, y)])
    visited[x][y] = True
    current_color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 적록색약인 경우 R과 G를 동일하게 취급
                if color_blind:
                    if (current_color in "RG" and grid[nx][ny] in "RG") or (current_color == "B" and grid[nx][ny] == "B"):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                # 일반적인 경우 같은 색만 탐색
                else:
                    if grid[nx][ny] == current_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

# 두 가지 경우의 방문 배열
visited_normal = [[False] * N for _ in range(N)]
visited_color_blind = [[False] * N for _ in range(N)]

normal_count, color_blind_count = 0, 0

# 일반적인 경우 탐색
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(i, j, visited_normal, color_blind=False)
            normal_count += 1

# 적록색약인 경우 탐색
for i in range(N):
    for j in range(N):
        if not visited_color_blind[i][j]:
            bfs(i, j, visited_color_blind, color_blind=True)
            color_blind_count += 1

# 출력
print(normal_count, color_blind_count)
