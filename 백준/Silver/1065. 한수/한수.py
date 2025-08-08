N = int(input())
count = 0

def hansu():
    hansu_budea = []
    plus_hansu=[]
    
    for i in range(1, 10):        
        hansu_budea.append(i*100+i*10+i)

        if i+2 < 10:
            hansu_budea.append(i*100 + (i+1)*10 + (i+2))
            hansu_budea.append((i+2)*100 + (i+1)*10 + i)
        else:
            continue

        if i+4 <10:
            hansu_budea.append(i*100+(i+2)*10+i+4)
            hansu_budea.append((i+4)*100+(i+2)*10+i)
        else:
            continue
        
        if i+6 <10:
            hansu_budea.append(i*100+(i+3)*10+i+6)
            hansu_budea.append((i+6)*100+(i+3)*10+i)
        else:
            continue
        
        if i+8 <10:
            hansu_budea.append(i*100+(i+4)*10+i+8)
            hansu_budea.append((i+8)*100+(i+4)*10+i)
        else:
            continue
        

    hansu_budea.append(210)
    hansu_budea.append(420)
    hansu_budea.append(630)
    hansu_budea.append(840)

    plus_hansu = sorted(set(hansu_budea))
    return plus_hansu

if N < 100:
    print(f'{N}')
elif N >= 100 and N <= 1000:
    
    for i in hansu():
        if N >= i:
            count +=1
        else:
            break
    print(f'{count+99}')
