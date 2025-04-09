import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

forbidden = set()

for i in range(M):
    forbidden.add(int(input()))

if 2 in forbidden:
    print(-1)
    sys.exit()

MAX_K = 150

visited = [[False] * (MAX_K + 1) for _ in range(N + 1)]

q = deque()
q.append((2, 1, 1))  # (위치, 직전 점프 길이, 점프 횟수)
visited[2][1] = True

while q:
    pos, k, steps = q.popleft()

    if pos == N:
        print(steps)
        sys.exit()

    for nk in [k - 1, k, k + 1]:
        if nk <= 0:
            continue
        next_pos = pos + nk
        if next_pos <= N and next_pos not in forbidden and not visited[next_pos][nk]:
            visited[next_pos][nk] = True
            q.append((next_pos, nk, steps + 1))

print(-1)