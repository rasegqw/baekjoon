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
