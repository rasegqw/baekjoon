# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())

# tree = {1: []}
# keep = deque()
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     if a in tree :
#         tree[a].append(b)
#         tree[b] = []
#     elif b in tree :
#         tree[b].append(a)
#         tree[a] = []
#     else:
#         keep.append([a, b])


# tree = {}
# for i in range(N):
#     a, b = map(int, input().split())
#     if a not in tree:
#         tree[a] = [b]
#         tree[b].append(a)
#     elif b not in tree:
#         tree[b] = [a]
#         tree[a].append(b)
#     else:
#         tree[a].append(b)
#         tree[b].append(a)



# while keep:
#     a = keep[-1][0]
#     b = keep[-1][1]
#     if a in tree :
#         tree[a].append(b)
#         tree[b] = []
#         keep.pop()
#     elif b in tree :
#         tree[b].append(a)
#         tree[a] = []
#         keep.pop()        
#     else:
#         keep.rotate(1)

# ans = [0]*N
# for i in tree:
#     for j in tree[i]:
#         ans[j-1] = i

# for i in ans[1:]:
#     print(i)


from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

tree = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (N + 1)  
queue = deque([1])  
visited = set([1])  

while queue:
    node = queue.popleft()
    for child in tree[node]:  # 현재 노드의 연결된 노드들 탐색
        if child not in visited:  # 방문하지 않은 노드만 처리
            parent[child] = node  # 현재 노드가 자식 노드의 부모가 됨
            visited.add(child)
            queue.append(child)

for i in range(2, N + 1):
    print(parent[i])
