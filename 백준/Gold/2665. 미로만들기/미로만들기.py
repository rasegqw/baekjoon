from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = 0  # 벽 부순 개수

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않았거나 더 적게 부순 경우
                if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + (1 if graph[nx][ny] == 0 else 0):
                    if graph[nx][ny] == 1:  # 흰 방은 그냥 이동
                        visited[nx][ny] = visited[x][y]
                        dq.appendleft((nx, ny))  # 0비용 → 앞에 넣기
                    else:  # 검은 방은 부숴야 함
                        visited[nx][ny] = visited[x][y] + 1
                        dq.append((nx, ny))  # 1비용 → 뒤에 넣기

bfs()
print(visited[N-1][N-1])
