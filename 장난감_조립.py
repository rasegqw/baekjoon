# from collections import deque

# N = int(input())

# M = int(input())

# qnvna = [[0 for _ in range(N+1)]] * (N+1)

# for i in range(M):
#     x, y, z = map(int, input().split())
#     qnvna[x][y] = z

# collect = deque([N, 1])
# count = 0
# while collect:
#     now, mul_count = collect.popleft()
#     for i in range(1, N+1):
#         if qnvna[now][i] == 0:
#             continue
#         else:            
#             count_collect = mul_count * qnvna[now][i]
            
#             collect.append([i, count_collect])


from collections import deque

N = int(input())  # 부품 개수
M = int(input())  # 관계 개수

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

# 각 부품을 만들기 위해 필요한 부품 정보 저장
for _ in range(M):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))  # y를 사용해서 x를 만듬
    indegree[x] += 1

# dp[i][j]: i를 만들기 위해 j가 몇 개 필요한가
dp = [[0] * (N+1) for _ in range(N+1)]

q = deque()

# 기초 부품은 indegree가 0
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i][i] = 1  # 자기 자신 1개 필요

while q:
    now = q.popleft()
    for next, count in graph[now]:
        # 다음 부품을 만들기 위해 현재 부품의 기초 부품 수를 누적
        for i in range(1, N+1):
            dp[next][i] += dp[now][i] * count
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

# 완제품 N번을 만들기 위해 필요한 기초 부품만 출력
for i in range(1, N+1):
    if dp[N][i] > 0:
        print(i, dp[N][i])
