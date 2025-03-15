N = int(input())

num=[]

for i in range(N):
    num.append(int(input()))

a = sorted(set(num))

for i in a:
    print(f'{i}')