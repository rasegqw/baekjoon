from collections import deque

M, N, H = map(int, input().split())
tomaeto_box = []

for i in range(H):
    a = [list(map(int, input().split())) for _ in range(N)]
    tomaeto_box.append(a)

good_tomaeto = deque()   # (H, N, M) 순서로 저장할 거

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomaeto_box[i][j][k] == 1:
                good_tomaeto.append((i, j, k))

while good_tomaeto:
    h, n ,m = good_tomaeto.popleft()

    for i in range(6):
        next_h = h + dz[i]
        next_n = n + dy[i]
        next_m = m + dx[i]
        if next_h < 0 or next_h >= H or  next_n < 0 or  next_n >= N or next_m < 0 or next_m >= M:
            continue

        cur = tomaeto_box[next_h][next_n][next_m]
        if cur == 0:
            tomaeto_box[next_h][next_n][next_m] = tomaeto_box[h][n][m] + 1
            good_tomaeto.append((next_h, next_n, next_m))

count = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomaeto_box[i][j][k] == 0:
                print(-1)
                exit()
            count = max(count, tomaeto_box[i][j][k])

print(count - 1)