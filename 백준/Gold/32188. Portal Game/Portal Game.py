import sys
from collections import deque

input = sys.stdin.readline
INF = 1<<50

def solution(v1, v2):
    N, C = v1
    # print(N, C)

    rp = {}
    bp = {}


    visited = [False] * N

    for portal in v2:
        if portal[0] == 1:
            bp[portal[1]] = portal[2]
        else:
            rp[portal[1]] = portal[2]

    q = deque([[0, 0]])     # cur, t
    
    min_t = INF

    while q:
        cur, t = q.popleft()
        
        if visited[cur] == False:
            visited[cur] = True
        else:
            continue

        if cur >= N-1:
            min_t = min(min_t, t)
            continue
        if t >= min_t:
            continue

        if cur in bp:
            if visited[cur+1] == False:
                q.append([cur+1, t+1])
            if visited[bp[cur]] == False:
                q.appendleft([bp[cur], t])

        elif cur in rp:
            if visited[rp[cur]] == False:
                q.appendleft([rp[cur], t])

        else:
            if visited[cur+1] == False:
                q.append([cur+1, t+1])
        
        # print(q)

    if min_t == INF:
        return -1
    else:
        return min_t


if __name__=="__main__":
    v1 = list(map(int, input().split()))
    v2 = []

    for _ in range(v1[1]):
        v2.append(list(map(int, input().split())))

    print(solution(v1=v1, v2=v2))