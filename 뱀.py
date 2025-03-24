import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

Anum = int(input())
Apple = [0] * Anum

for i in range(Anum):
    Apple[i] = list(map(int, input().split()))
    Apple[i][0] -= 1
    Apple[i][1] -= 1

Lcount = int(input())
Ltime = []
Ldirec = deque()
for i in range(Lcount):
    time, direc = map(str, input().split())
    time= int(time)
    Ltime.append(time)
    Ldirec.append(direc)

Timecount = 0

snake = [[0, 0]]
vec = [0, 1]  # [y, x]
isGood = True

while isGood:
    Timecount += 1
    # snake_body = deque([])
    new_head = []

    # vec 방향에 따라 진행
    # for i in snake:
    #     a = copy.deepcopy(i)
    #     new_head.append(a)
    
    new_head.append(snake[0][0] + vec[0])
    new_head.append(snake[0][1] + vec[1])
    snake.insert(0, new_head)
    
    # for i in range(1, len(snake)):
    #     snake[i] = snake_body.popleft()
    
        
    # 진행한 공간이 벽인지 판단
    if new_head[0] >= N or new_head[0] < 0 or new_head[1] >= N or new_head[1] < 0:
        break

    # 진행한 공간에 자기 자신이 있는지 판단
    if new_head in snake[1:]:
        break

    # 진행한 공간에 사과가 있는지 판단
    if snake[0] in Apple:
        Apple.remove(snake[0])
    else:
        snake.pop()

    # if new_head in snake[1::]:
    #     break
    


    # 방향을 바꿀것인지 판단
    if Timecount in Ltime:
        if Ldirec.popleft() == 'D':
            vec = [vec[1], -vec[0]]
            # if vec ==[0,1]:
            #     vec = [1, 0]
            # elif vec == [1, 0]:
            #     vec = [0, -1]
            # elif vec == [-1, 0]:
            #     vec = [0, 1]
            # else:
            #     vec = [-1, 0]
        else:
            vec = [-vec[1], vec[0]]
            # if vec == [0,1] :
            #     vec = [-1, 0]
            # elif vec == [1, 0]:
            #     vec = [0,1]
            # elif vec == [-1, 0]:
            #     vec = [0, -1]
            # else:
            #     vec = [1, 0]

    # timecount += 1

print(Timecount)