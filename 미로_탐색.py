from collections import deque

N, M = map(int, input().split())

Board = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_route(x, y):
    visited = deque()
    visited.append([x, y])

    while visited:
        a = visited.popleft()
        for i in range(4):
            nx = a[0] + dx[i]
            ny = a[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if Board[nx][ny] == 0 :
                continue

            if Board[nx][ny] == 1 :
                Board[nx][ny] = Board[a[0]][a[1]] + 1
                visited.append([nx, ny])

    return Board[N-1][M-1]

print(find_route(0, 0))

