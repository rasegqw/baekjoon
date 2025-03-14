A = input()
A=int(A)

def FourT(a):
    if (a%4) == 0 :
        return True
    else :
        return False 


def HundT(a):
    if (a%100) == 0 :
        return True
    else :
        return False



def Yoon(x):
    if FourT(x) == True and HundT(x) == False:
        return 1
    elif (x%400) == 0 :
        return 1
    else :
        return 0
        
print(f"{Yoon(A)}")