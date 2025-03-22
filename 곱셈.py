from itertools import product

A, B, C = map(int, input().split())


# for i in

i = 0
while A>=2**i :
    i += 1

A -= 2**(i-1)
move = [i-1]
if A != 0:        
    for j in range(1, i):
        if A >= 2**(i-j-1):
            A -= 2**(i-j-1)
            move.append(i-j-1)
            if A == 0:
                break

res = 0

for c in product(range(len(move)), repeat=B):
    total = sum(move[i] for i in c)
    res += 1 << total



print(res%C)

