import heapq
import sys

N = int(input())
upper_mid = []
under_mid = []
under_mid.append(-int(sys.stdin.readline()))
print(-under_mid[0])

if N == 1:
    exit()

else:
    for i in range(1, N):
        num = int(sys.stdin.readline())
        if num <= -under_mid[0]:
            heapq.heappush(under_mid, -num)
        else:
            heapq.heappush(upper_mid, num)

        if len(upper_mid) > len(under_mid) :
            heapq.heappush(under_mid, -heapq.heappop(upper_mid))
        elif len(under_mid) - len(upper_mid) > 1 :
            heapq.heappush(upper_mid, -heapq.heappop(under_mid))

        print(-under_mid[0])

# import heapq
# import sys

# input = sys.stdin.readline
# N = int(input())

# max_heap = []
# min_heap = []

# # 첫 번째 입력 처리
# num = int(input())
# heapq.heappush(max_heap, -num)
# print(num)

# for _ in range(1, N):
#     num = int(input())

#     # 중간값 유지 위해 max_heap에 먼저 넣음
#     if num <= -max_heap[0]:
#         heapq.heappush(max_heap, -num)
#     else:
#         heapq.heappush(min_heap, num)

#     # 힙 크기 조정
#     if len(max_heap) > len(min_heap) + 1:
#         heapq.heappush(min_heap, -heapq.heappop(max_heap))
#     elif len(min_heap) > len(max_heap):
#         heapq.heappush(max_heap, -heapq.heappop(min_heap))

#     print(-max_heap[0])
