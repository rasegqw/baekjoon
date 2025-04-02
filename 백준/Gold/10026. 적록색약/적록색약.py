# 적록 색약
import heapq
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

grid = []
for _ in range(N):
    a = list(map(str, input().strip()))
    grid.append(a)

def R_G_B():
    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
    
        if rootA != rootB:
            for i in range(N**2):
                if parents[i] == rootB:
                    parents[i] = rootA 

    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    stack = [[0, 0]]    # y, x
    
    parents = [i for i in range(N**2)]
    
    visited = [[False for _ in range(N)] for g in range(N)]

    while stack:
        x, y = heapq.heappop(stack)
        
        if visited[y][x] == True:
            continue
        visited[y][x] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if grid[ny][nx] == grid[y][x]:
                    union(y*N + x, ny*N + nx)
                heapq.heappush(stack, [ny, nx])

    res = set(parents)
    return len(res)


def RG_B():
    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
    
        if rootA != rootB:
            for i in range(N**2):
                if parents[i] == rootB:
                    parents[i] = rootA 

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    stack = [[0, 0]]    # y, x
    
    parents = [i for i in range(N**2)]

    visited = [[False for _ in range(N)] for g in range(N)]

    while stack:
        x, y = heapq.heappop(stack)

        if visited[y][x] == True:
            continue

        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if (grid[ny][nx] == grid[y][x]) or (grid[ny][nx] == 'R' and grid[y][x] == 'G') or (grid[ny][nx] == 'G' and grid[y][x] == 'R'):
                    union(y*N + x, ny*N + nx)
                heapq.heappush(stack, [ny, nx])


    res = set(parents)
    return len(res)


print(R_G_B(), RG_B())