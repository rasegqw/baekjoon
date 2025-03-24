import heapq
import sys

N = int(sys.stdin.readline())
H = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    H.append((min(a, b), max(a, b)))

D = int(sys.stdin.readline())

# 끝점을 기준으로 정렬
H.sort(key=lambda x: x[1])

heap = []
max_count = 0

for start, end in H:
    # 현재 시작점을 힙에 추가
    heapq.heappush(heap, start)
    
    # 철로 범위를 벗어나는 시작점 제거
    while heap and heap[0] < end - D:
        heapq.heappop(heap)
    
    # 현재 힙의 크기가 구간 내 사람 수
    max_count = max(max_count, len(heap))

print(max_count)
