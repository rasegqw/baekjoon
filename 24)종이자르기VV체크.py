w, h = map(int, input().split(' '))

T = int(input())

x = [w]
y = [h]

for i in range(T):
    xy, l = map(int, input().split(' '))
    if xy ==0:
        y.append(l)
    else:
        x.append(l)

x = sorted(x)
y = sorted(y)
width = [x[0]]
height = [y[0]]

for i in range(len(x)-1):
    width.append(x[i+1]-x[i])

for i in range(len(y)-1):
    height.append(y[i+1]-y[i])

print(f'{max(width)*max(height)}')
