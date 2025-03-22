N = int(input()) 

ans = []
for i in range(N):
    S = int(input())
    if S == 1:
        ans.append(1)
    elif S == 2:
        ans.append(2)
    elif S == 3:
        ans.append(4)    
    
    
    else:
        res = [None] * S
        res[0] = 1
        res[1] = 2
        res[2] = 4
        for j in range(S-3):
            res[j+3] = res[j] + res[j+1] + res[j+2]
        ans.append(res[S-1])

for i in range(len(ans)):
    print(ans[i])