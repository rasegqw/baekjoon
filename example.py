from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for w in range(V+1)]
    for t in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    Black = set()
    White = set()
    que = deque([a])
    Black.add(a)
    visited = [False] * (V+1)
    idx = 0

    while que:
        x = que.popleft()
        visited[x] = True

        for i in graph[x]:
            if i in Black or i in White:
                if (i in Black and x in Black) or (i in White and x in White):
                    print('NO')
                    Black = set()
                    White = set()
                    que = []
                    break
                else:
                    if not que and False in visited[1:]:
                        idx = visited[1:].index(False) + 1
                        que.append(idx)
                    continue
            if x in Black:
                White.add(i)
            else:
                Black.add(i)
            if visited[i] == True:
                continue
            que.append(i)
    
    for i in Black:
        if i in White:
            print('NO')
            exit()
    if len(Black) + len(White) != 0:
        print('YES')