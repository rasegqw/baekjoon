Nanj = []
totalk = 0
for i in range(9):
    Nanj.append(int(input()))
    totalk += Nanj[i]

bumin2 = totalk - 100

for i in Nanj:
    for j in Nanj:
        if i == j :
            continue
        elif (i + j) == bumin2:
            Nanj.remove(i)
            Nanj.remove(j)
            break
    if len(Nanj) == 7:
        break

Nanj.sort()
for i in Nanj:
    print(i)