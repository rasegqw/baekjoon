T = int(input())

# 소수 판단.
def sosu(x):
    for i in range(1, int(((x)**(1/2))//1)):
        if x % (i+1) == 0:
            # 소수가 아님.
            return False
    return True
    

def goldbah():
    n = int(input())
    for i in range(int((n/2)//1)):
        if sosu(int(n/2)-i) and sosu(int(n/2)+i):
            print(f'{int(n/2)-i} {int(n/2)+i}') 
            break       

for i in range(T):
    goldbah()



