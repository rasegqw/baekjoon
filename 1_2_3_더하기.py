N = int(input())

a = []
result = 0
One_Two_Three = []

count = [0] * N


def factorial(a):
    fac = 1
    if a == 0:
        return 1
    for i in range(1, a+1):
        fac *= i
    return fac

def guhagi(num1, num2, num3, i):
    global count
    count[i] += int(factorial(num1+num2+num3) / (factorial(num1)*factorial(num2)*factorial(num3)))


for i in range(N):

    a.append(int(input()))

    One_Two_Three = [0] * 3
    One_Two_Three[2] = a[i] // 3



    if a[i] %3 != 0:
        One_Two_Three[a[i]%3-1] += 1 

    guhagi(One_Two_Three[0], One_Two_Three[1], One_Two_Three[2],i)

    if a[i]%2 == 0:
        for j in range(a[i]//2-a[i]//3):
            guhagi(2*j,a[i]//2-j,0,i)
    elif One_Two_Three[0]>=1 and One_Two_Three[2]>=1:
        guhagi(One_Two_Three[0]-1, One_Two_Three[1]+2, One_Two_Three[2]-1, i)
        
    for j in range(1, a[i]//3 + 1):
        guhagi(One_Two_Three[0]+j, One_Two_Three[1]+j, One_Two_Three[2]-j,i)
        
        if One_Two_Three[0]+j>=1 and One_Two_Three[2]-j>=1:
            guhagi(One_Two_Three[0]+j-1, One_Two_Three[1]+j+2, One_Two_Three[2]-j-1, i)
       
        for k in range(1, One_Two_Three[1]+j+1):
            guhagi(One_Two_Three[0]+j+2*k, One_Two_Three[1]+j-k, One_Two_Three[2]-j,i)
        
                # if One_Two_Three[0]+j+2*k>=1 and One_Two_Three[2]-j:
                #     guhagi(One_Two_Three[0]+j+2*k-1, One_Two_Three[1]+j-k+2, One_Two_Three[2]-j-1, i)
        




    # One_Two_Three[0], One_Two_Three[1], One_Two_Three[2] = a[i]%2, a[i]//2, 0
    #     # count[i] += 1
    # for j in range(a[i]//2 - a[i]//3):
    #     guhagi(One_Two_Three[0]+2*j, One_Two_Three[1]-j, 0,i)

    print(count[i])