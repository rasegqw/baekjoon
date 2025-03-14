num1 = int(input())
num2 = int(input())
num3 = int(input())

ans = str(num1*num2*num3)

for i in range(10):
    c = ans.count(f'{i}')
    print(f'{c}')