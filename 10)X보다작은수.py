NX = input()
num = NX.split(" ")
N = int(num[0])
X = int(num[1])
# map

AAA = input()
A = AAA.split(" ")

for i in range(len(A)):
    A[i] = int(A[i])

def Versus(a, b):
    if a>=b :
        return False
    else:
        return True

ANS = []

for i in range(len(A)):
    if Versus(A[i], X) :
        A[i] = str(A[i])
        ANS.append(A[i])

print(' '.join(ANS)) 

# print(ans[i], end='') end='' ---> ' '로 붙이기 