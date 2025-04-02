# 줄 세우기 (위상 정렬)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

student = [[] for _ in range(N+1)]
indegree = [ 0 for _ in range(N+1) ]    # 진입차수 체크

for i in range(M):
    a, b = map(int, input().split())
    student[a].append(b)
    indegree[b] += 1

que = deque()
result = []

for i in range(1, N+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    x = que.popleft()
    result.append(x)

    for i in student[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)
        
for i in result:
    print(i, end = ' ')