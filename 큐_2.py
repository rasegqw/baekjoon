from collections import deque
import sys

N = int(input())

que = deque()

# find 함수는 해당 값을 찾으면, 인덱스를 불러옴
# 못찾으면 -1 불러옴
for i in range(N):
    a = sys.stdin.readline().strip()
    if a.find('pu') != -1:
        que.append(a.split()[1])
    elif a == 'back' :
        if len(que) != 0:        
            print(que[-1])
        else:
            print(-1)
    elif a =='front' :
        if len(que) != 0:        
            print(que[0])
        else:
            print(-1)            
    elif a == 'size':  
        print(len(que))
    elif a == 'empty' :
        if len(que)>0:
            print(0)
        else:
            print(1)
    else:             # pop. FIFO
        if len(que) != 0:
            print(que.popleft())         
        else:
            print(-1)
