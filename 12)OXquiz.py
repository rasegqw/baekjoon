num = int(input())

def score(a):
    O = a.replace('X',' ')
    OX = O.split(' ')
    real_ANS = 0
    ans = 0
    for i in range(len(OX)):
        if OX[i] == ' ':
            return
        else:
            real_ANS += _score(OX[i])
    
    return real_ANS

def _score(b):
    ans = 0
    for i in range(len(b)):
        ans += i+1
    
    return ans

for i in range(num):
    AAA = input()
    print(f"{score(AAA)}")