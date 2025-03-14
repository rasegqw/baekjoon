ABV = input()
x=[]
for i in range(3):
    x.append(int(ABV.split(' ')[i]))

if (x[2]-x[0])%(x[0]-x[1]) ==0 : 
    day = (x[2]-x[0])//(x[0]-x[1])
else:
    day = (x[2]-x[0])//(x[0]-x[1])+1

print(f"{day+1}")