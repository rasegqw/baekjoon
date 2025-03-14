two_num = input()
num = two_num.split(' ')

ans = ''
sang_num = []

for i in num:
    # _num = []
    # for k in i:
    #     _num.append(k)
    # ans = _num[0:3:-1]
    ans = i[2::-1]
#   ans = _num[2]+_num[1]+_num[0]
    sang_num.append(int(ans))

if(sang_num[0]>sang_num[1]):
    print(sang_num[0])
else:
    print(sang_num[1])

# 슬라이싱
# a[start:end:step]
# start = 슬라이싱 시작할 위치
# end   = end-1까지 슬라이싱
# step  = 보폭. 몇개씩 갈지.
# 만약 이번 문제처럼 end = -1을 넣고 싶을땐, 그냥 비워두면 됨.
# ex) i[2:-1:-1] -- X, i[2::-1] -- O