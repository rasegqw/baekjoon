import heapq

N = int(input())
board = []

for _ in range(N):
    a = list(map(int, input().strip()))
    board.append(a)

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

heap = [[0, 0, 0]]

res = 0
visited = [[False for _ in range(N)] for j in range(N)]

while heap:
    dist, y, x = heapq.heappop(heap)
    
    if visited[y][x] == True:
        continue
    
    visited[y][x] = True

    if y == N-1 and x == N-1:
        res = dist
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N:
            if board[ny][nx] == 0 :
                heapq.heappush(heap, [dist+1, ny, nx])
            else:
                heapq.heappush(heap, [dist, ny, nx])


print(res)