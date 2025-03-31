# from collections import deque

# R, C = map(int, input().split())

# place = []
# water = []
# for _ in range(R):
#     a = list(map(str, input().split()))
#     place.append(a)


# for i in range(R):
#     for j in range(C):
#         if place[i][j] == 'D':
#             start = (i, j)      # y, x
#         if place[i][j] == 'S':
#             end = (i, j)
#         if place[i][j] == '*':
#             water.append((i, j))    # y, x
# count = 0
# que  = deque((count, start))
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# min_count = 1 << 10

# while que:
#     n_count, current = que.popleft()
#     if current == end:
#         min_count = min(min_count, n_count)
#         break

#     n_count += 1
#     for i in range(4):
#         nx = current[1] + dx[i]
#         ny = current[0] + dy[i]

#         if place[ny][nx] == '.':
#             que.append((n_count, (ny, nx)))
#         elif place[ny][nx] == '*' or place[ny][nx] == 'X':

#         else:

import sys
from collections import deque

input = sys.stdin.read
dx = [-1, 1, 0, 0]  # 상하좌우 이동
dy = [0, 0, -1, 1]

def bfs():
    while water_queue or hedgehog_queue:
        # 1️⃣ 물 먼저 이동
        for _ in range(len(water_queue)):
            x, y = water_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and not water_time[nx][ny]:
                    if forest[nx][ny] == '.':  # 물이 이동 가능하면 확산
                        water_time[nx][ny] = water_time[x][y] + 1
                        water_queue.append((nx, ny))

        # 2️⃣ 고슴도치 이동
        for _ in range(len(hedgehog_queue)):
            x, y, time = hedgehog_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if forest[nx][ny] == 'D':  # 비버의 굴 도착
                        print(time + 1)
                        return
                    if forest[nx][ny] == '.' and not visited[nx][ny]:
                        if not water_time[nx][ny] or time + 1 > water_time[nx][ny]:  # 물보다 먼저 도착 가능
                            visited[nx][ny] = True
                            hedgehog_queue.append((nx, ny, time + 1))

    print("KAKTUS")  # 도달 불가능

# 입력 처리
data = input().split()
R, C = map(int, data[:2])
forest = []
water_queue = deque()
hedgehog_queue = deque()
water_time = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

index = 2
for i in range(R):
    row = list(data[index])
    index += 1
    forest.append(row)
    for j in range(C):
        if row[j] == 'S':  # 고슴도치 위치
            hedgehog_queue.append((i, j, 0))
            visited[i][j] = True
        elif row[j] == '*':  # 물 위치
            water_queue.append((i, j))
            water_time[i][j] = 1  # 물이 찰 시간 기록

bfs()
