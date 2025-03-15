N = int(input())

a = 1
b = 2
c = 3
count = 0

x =0
for i in range(N):
    x += 2**i

def hanoi(num, start, step, end):    
    if num == 2:
        print(f'{start} {step}')
        print(f'{start} {end}')
        print(f'{step} {end}')
    else:
        hanoi(num-1, start, end, step)
        print(f'{start} {end}')
        hanoi(num-1, step, start, end)

# def quiet(num, start, step, end):
#     global count
    
#     if num == 2:
#         count += 3
#     else:
#         quiet(num-1, start, end, step)
#         count += 1
#         quiet(num-1, step, start, end)        

print(x)

# hanoi(N, a, b, c)
# print(f'{count}')
if N <= 20:
    hanoi(N, a, b, c)
