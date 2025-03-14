two_num = input()
num = two_num.split(' ')

ans = ''
sang_num = []

for i in num:
    _num = []
    for k in i:
        _num.append(k)
    ans = _num[2]+_num[1]+_num[0]
    sang_num.append(int(ans))

if(sang_num[0]>sang_num[1]):
    print(sang_num[0])
else:
    print(sang_num[1])

# 슬라이싱