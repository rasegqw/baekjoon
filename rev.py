# from collections import deque
# N, M = map(int,input().split())
# Map = []
# for _ in range(N):
#     Map.append(list(map(str, input().strip())))

# count = 0

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# checker = set((0,0))
# Q = deque([[0, 0, Map[0][0]]])

# while Q:
#     x, y, t = Q.popleft()

#     for i in range(4):
#         nx = x +dx[i]
#         ny = y + dy[i]

#         if 0 <= nx <N and 0<=ny <N:

#             if t == '-'  and (y,nx) not in checker :
#                 if Map[y][nx] != '-':
#                     count += 1
#                 checker.add((y,nx))
#                 Q.append((y,nx,Map[y][nx]))

#             elif t == 'ㅣ' and (ny,x) not in checker:
#                 if Map[ny][x] != '|'  :
#                     count += 1
#                 checker.add((ny,x))
#                 Q.append((ny,x,Map[ny][x]))

# print(count)



# from collections import deque

# N, K = map(int,input().split())
# Map = []
# for _ in range(N):
#     Map.append(list(map(int,input().split())))

# S, X, Y = map(int,input().split())
# Q = deque([(X-1,Y-1)])
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# checker = set()
# check = set()
# count = 0
# while count < S:

#     (y,x) = Q.popleft()

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx <N and 0<=ny <N and (ny, nx) not in check:
#             if Map[ny][nx] != 0:
#                 checker.add(Map[ny][nx])
#             Q.append((ny,nx))
#             check.add((ny,nx))

#     count += 1

# if not checker:
#     print(0)
# else:
#     print(max(checker))


# from collections import deque
# import sys
# N = int(sys.stdin.readline())
# checker = set()
# Map = []
# for i in range(N):
#     a = sys.stdin.readline().strip()
#     l = []
#     for j in range(N):
#         l.append(int(a[j]))
#         if int(a[j]) == 1:
#             checker.add((i,j))
#     Map.append(l)
# result = []


# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# while checker:
#     Q = deque([(next(iter(checker)))])
#     count = 0
#     while Q:
#         (y, x) = Q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx <N and 0<=ny <N and Map[ny][nx] == 1 and (ny, nx) in checker:
#                 count += 1
#                 Q.append((ny,nx))
#                 checker.discard((ny,nx))

#     result.append(count)

# print(len(result))
# for i in sorted(result):
#     sys.stdout.write(str(i))

a = [10] * 10
b = a[1]

a[3] = 2
print(a)