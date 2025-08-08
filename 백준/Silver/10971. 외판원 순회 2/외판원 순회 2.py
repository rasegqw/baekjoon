import sys

input = sys.stdin.readline

n = int(input())
world = []

visited = [False] * n
min_res = 1 << 24

for i in range(n):
    x = list(map(int, input().split()))
    world.append(x)


def backtrace(start, now, cnt, cost_sum):
    global min_res

    if cost_sum > min_res:
        return
    
    if cnt == n and world[now][start] != 0:
        cost_sum += world[now][start]
        min_res = min(min_res, cost_sum)
        return 

    for next in range(n):
        if visited[next] == False and world[now][next] != 0:
            visited[next] = True
            backtrace(start, next, cnt+1, cost_sum + world[now][next])
            visited[next] = False

for i in range(n):
    visited[i] = True
    backtrace(i, i, 1, 0)
    visited[i] = False

print(min_res)