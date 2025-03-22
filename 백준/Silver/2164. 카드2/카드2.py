from collections import deque
import sys

N = int(input())

que = deque(range(1, N+1))
count = N

if N == 1 :
    print(que.pop())
else:
    while True:
        que.popleft()
        count -= 1
        if count == 1:
            break
        que.append(que.popleft())
    print(que.pop())