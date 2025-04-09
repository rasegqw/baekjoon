import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]  # -1이면 아직 방문 안 함

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 목적지 도달
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0  # 초기화: 가능한 경로 수 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:  # 내리막길 조건
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
