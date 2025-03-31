# import sys
# input = sys.stdin.readline

# N = int(input())

# a = input().strip()
# place = [0]

# for i in a:
#     place.append(int(i))

# if place.count(1) < 2:
#     print(0)
#     exit()

# edge = [ [] for _ in range(N+1)]

# for _ in range(N-1):
#     A, B = map(int, input().split())

#     edge[A].append(B)
#     edge[B].append(A)    

# cur = []
# count = 0
# for i in range(1, N+1):
#     if place[i] == 0:
#         continue
#     cur.append(i)
#     visited = []
#     while cur:
#         a = cur.pop()
#         visited.append(a)
#         for j in edge[a]:
#             if j in visited:
#                 continue
#             if place[j] == 1:
#                 count += 1
#             else:
#                 cur.append(j)

# print(count)
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.read

def dfs(node):
    stack = [node]
    visited.add(node)
    count = 0  # 실내 노드 개수

    while stack:
        cur = stack.pop()
        for neighbor in graph[cur]:
            if neighbor in visited:
                continue
            if indoor[neighbor - 1] == 1:  # 실내 노드라면 카운트 증가
                count += 1
            else:  # 실외 노드라면 계속 탐색
                visited.add(neighbor)
                stack.append(neighbor)
    
    return count

# 입력 처리
data = input().split()
n = int(data[0])
indoor = list(map(int, list(data[1][:n])))  # 실내(1), 실외(0) 정보
edges = list(map(int, data[2:]))  # 간선 정보

# 그래프 구성
graph = [[] for _ in range(n + 1)]
for i in range(0, len(edges), 2):
    u, v = edges[i], edges[i + 1]
    graph[u].append(v)
    graph[v].append(u)

# 1. 실내(1) 노드끼리 직접 연결된 경우 카운트
result = 0
for i in range(1, n + 1):
    if indoor[i - 1] == 1:  # 실내 노드라면
        for neighbor in graph[i]:
            if indoor[neighbor - 1] == 1:  # 실내-실내 연결
                result += 1
# result //= 2  # 중복 계산 제거

# 2. 실외(0) 노드를 거치는 경우 계산
visited = set()
for i in range(1, n + 1):
    if indoor[i - 1] == 0 and i not in visited:  # 실외 노드면서 방문하지 않은 경우
        cnt = dfs(i)
        result += cnt * (cnt - 1)  # 두 노드 선택 방법

print(result)
