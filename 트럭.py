# import sys
# from collections import deque
# input = sys.stdin.readline

# N, W, L = map(int, input().split())
# # N : 트럭의 수, W : 다리 길이, L : 다리 최대 하중

# truck = deque(map(int, input().strip().split()))


# total = L
# time = 0
# go = deque()

# while True:
#     time += 1
#     if len(go) == W:
#         total += go.popleft()

#     if total - truck[0] >= 0:
#         go.append(truck.popleft())
#         total -= go[-1]
#     else:


#     # 어떻게 출발한 시각과 도착한 시간을 이용하지?
    
        
        
        
        
        
#         if len(go) == W:
#             break
#         else:
#             break


#     time += W + len(go) - 1
#     go = []
#     total = 0

# time += 1

# print(time)
import sys
from collections import deque

input = sys.stdin.readline

N, W, L = map(int, input().split())
truck = list(map(int, input().strip().split()))

bridge = deque([0] * W)
current_weight = 0
time = 0

for t in truck:
    while True:
        current_weight -= bridge.popleft()

        if current_weight + t <= L:
            bridge.append(t)
            current_weight += t
            time += 1
            break
        else:
            bridge.append(0)
            time += 1


time += W

print(time)
