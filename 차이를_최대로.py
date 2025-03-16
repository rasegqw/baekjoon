# 내 알고리즘으로도 풀어보고 싶다...

from itertools import permutations

N = int(input())

# nums =[]
num = list(map(int, input().split()))
num.sort()

perm = list(permutations(num))


# for i in num:
#     for j in num:
#         nums.append({'index':i, 'diff':abs(i-j), 'diffindex':j})


# a = nums[N-1]['diff']
totalres = []

def ap(x, y):
    total =0
    for i in range(N-1):
        total += abs(y[i]-y[i+1])
    x.append(total)

for i in perm:
    for j in range(len(i)):
        ap(totalres, i)

print(f'{max(totalres)}')