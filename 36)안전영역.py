import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

Land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count2 = 0
visited = [[False] * N for _ in range(N)]
def fourD(x, y, z):
    if visited[y][x]:
        return
    visited[y][x] = True


    if x<N-1 and Land[y][x+1] > z :
        fourD(x+1, y, z)
    if y<N-1 and Land[y+1][x] > z:
        fourD(x, y+1, z)
    if x>0 and Land[y][x-1] > z:
        fourD(x-1, y, z)
    if y>0 and Land[y-1][x] > z:
        fourD(x, y-1, z)



for k in range(N):
    count = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(len(Land)):
        for j in range(len(Land[i])):
            if Land[i][j] > k and not visited[i][j]:
                fourD(j, i, k)
                count +=1

    count2 = max(count2, count)

print(count2)

    # for _ in range(4):
    #     if x<N-1 and Land[y][x+1] > z :
    #         fourD(x+1, y, z)
    #     elif y<N-1 and Land[y+1][x] > z:
    #         fourD(x, y+1, z)
    #     elif x>0 and Land[y][x-1] > z:
    #         fourD(x-1, y, z)
    #     elif y>0 and Land[y-1][x] > z:
    #         fourD(x, y-1, z)




    # for i in range(len(Land)):
    #     for j in range(len(Land[i])):
    #         if Land[i][j] > k+1:
    #             Land[i][j] = 1
    #         else:
    #             Land[i][j] = 0




        # if Land[i][j] == Land[i][j-1] and j>0:
        #     continue
        # elif Land[i][j] == Land[i-1][j] == 1 and i>0: # 열 같을 때
        #     continue
        # elif Land[i][j] ==1: # 행 같을때
        #     if j == N-1 or i == N-1:

            # count+=1



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
    

