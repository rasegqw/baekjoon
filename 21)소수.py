N = int(input())

nums = input()
num = nums.split()
a=[]
count = 0

for i in num:
    a.append(int(i))

m = int((max(a)**(1/2)) // 1)

for i in a:
    max_nanugi = int((i**(1/2))//1)

    for j in range(m):
        if i**(1/2) % 1 == 0:
            count += 1
            break
        elif max_nanugi != 1:
            for k in range(1, max_nanugi):
                if i % (k+1) == 0 :
                    count += 1
                    break
            break


print(f"{len(a) - count}")
