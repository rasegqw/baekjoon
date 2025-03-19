N = int(input())

square=[]
for i in range(N):
    a = list(map(int, input().split()))
    square.append(a)

countB = 0
countW = 0
def isAllSame(start_x, end_x, start_y, end_y):
    global countB, countW
    for i in range(start_x, end_x-1):
        for j in range(start_y, end_y-1):
            if square[i][j] != square[i][j+1] or square[i+1][j] != square[i+1][j+1] or square[i][j+1] != square[i+1][j] or square[i][j] != square[i+1][j+1]:
                return False
    
    if square[start_x][start_y] == 1:
        countB+=1
    else:
        countW+=1
    return True

def divide(start_x, end_x, start_y, end_y, n = N):
    global countB, countW
    if n == 1:
        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                if square[i][j] == 1:
                    countB+=1
                else:
                    countW+=1
        return

    if isAllSame(start_x, end_x, start_y, end_y):
        return

    else:
        n = n//2        # 여기 문제
        divide(start_x, start_x+n, start_y, start_y+n, n)
        divide(start_x+n, start_x+2*n, start_y, start_y+n, n)
        divide(start_x, start_x+n, start_y+n, start_y+2*n, n)
        divide(start_x+n, start_x+2*n, start_y+n, start_y+2*n, n)


divide(0,N,0,N)
print(countW)
print(countB)