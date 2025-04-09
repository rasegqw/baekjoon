from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

Toy = [0 for _ in range(N+1)]

for _ in range(M):
    x, y ,k = map(int, input().split())
    if type(Toy[x]) == int:
        Toy[x] = []
    Toy[x].append([y, k])

for i in range(1, N+1):
    if not Toy[i]:
        Toy[i] = 0

que = deque([[N, 1]])

while que:
    x, num = que.popleft()
    
    for i, count in Toy[x]:
        if type(Toy[i]) == int:
            Toy[i] += num*count
            continue
        que.append([i, num*count])

for i in range(1, N+1):
    if type(Toy[i]) == int:
        print(f'{i} {Toy[i]}')



# import sys
# from collections import deque

# # 입력
# N = int(sys.stdin.readline().strip())
# grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

# # 방향 벡터 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y, visited, color_blind):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     current_color = grid[x][y]

#     while queue:
#         cx, cy = queue.popleft()
        
#         for i in range(4):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 # 적록색약인 경우 R과 G를 동일하게 취급
#                 if color_blind:
#                     if (current_color in "RG" and grid[nx][ny] in "RG") or (current_color == "B" and grid[nx][ny] == "B"):
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))
#                 # 일반적인 경우 같은 색만 탐색
#                 else:
#                     if grid[nx][ny] == current_color:
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))

# # 두 가지 경우의 방문 배열
# visited_normal = [[False] * N for _ in range(N)]
# visited_color_blind = [[False] * N for _ in range(N)]

# normal_count, color_blind_count = 0, 0

# # 일반적인 경우 탐색
# for i in range(N):
#     for j in range(N):
#         if not visited_normal[i][j]:
#             bfs(i, j, visited_normal, color_blind=False)
#             normal_count += 1

# # 적록색약인 경우 탐색
# for i in range(N):
#     for j in range(N):
#         if not visited_color_blind[i][j]:
#             bfs(i, j, visited_color_blind, color_blind=True)
#             color_blind_count += 1

# # 출력
# print(normal_count, color_blind_count)



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, mode): 
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if not visited[nx][ny]:
                if arr[x][y] == arr[nx][ny]:
                    dfs(nx, ny, mode)
                elif mode == 1 and arr[x][y] == "R" and arr[nx][ny] == "G":
                    dfs(nx, ny, mode)
                elif mode == 1 and arr[x][y] == "G" and arr[nx][ny] == "R":
                    dfs(nx, ny, mode)

ans1 = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 0)
            ans1 += 1

ans2 = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 1)
            ans2 += 1

print(ans1, ans2)