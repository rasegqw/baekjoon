# import heapq
# import sys

# N = int(input())

# q=[]
# l = 0
# for i in range(N):
#     num = int(sys.stdin.readline().strip())
#     if i == 0:
#         heapq.heappush(q, [num, 1])

#     else:
#         l = len(q)
#         for j in range(l):
#             if q[j][0] == num:
#                 q[j][1] += 1
#                 break
#             elif j == l-1:
#                 heapq.heappush(q, [num, 1])



#     # q.put((int(sys.stdin.readline().strip())))
    
# for i in range(N):
#     num = heapq.heappop(q)
#     for j in range(num[1]):
#         print(num[0])

import heapq
import sys

N = int(input())

q = []  # 최소 힙 (숫자 저장)
count_map = {}  # 숫자 개수를 저장할 딕셔너리

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    
    if num in count_map:
        count_map[num] += 1  # 이미 있는 숫자라면 개수 증가
    else:
        count_map[num] = 1
        heapq.heappush(q, num)  # 새로운 숫자라면 힙에 추가

# 정렬된 값 출력
while q:
    num = heapq.heappop(q)  # 가장 작은 값을 꺼냄
    for _ in range(count_map[num]):  # 개수만큼 출력
        print(num)
