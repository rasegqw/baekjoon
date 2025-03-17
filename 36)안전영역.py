import sys

N = int(sys.stdin.readline())

Land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count =0
for i in Land:
    for j in range(len(i)):
        if i[j] > N:
            i[j] = 1
        else:
            i[j] =None

for i in range(len(Land)):
    for j in range(len(Land[i])):
        if Land[i][j] == Land[i][j-1] and j>0:
            continue
        elif Land[i][j] == Land[i-1][j] == 1 and i>0: # 열 같을 때
            continue
        elif Land[i][j] ==1: # 행 같을때
            count+=1


print(count)

# down_true = True
# right_true = True

# def right_check(x, y):
#     if Land[y][x] > N:
#         if x+1 == N:
#             down_check(x,y)
#             return
#         right_check(x+1,y)
#     else:
#         down_check(x, y)
#         return
    
# def down_check(x, y):
#     if Land[y][x] > N:
#         if y+1 == N:
#             count +=1
#             return
#         down_check(x,y+1)
#     else:
#             count +=1
#         return
    

