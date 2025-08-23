import sys

input = sys.stdin.readline

N = int(input())

target = [""] * N
target[0] = input()
length = len(target[0])

update = -1
for i in range(1, N):
    target[i] = input()

for i in range(length):
    res = set([])
    for j in target:
        res.add(j[i:])
    if len(res) != N:
        update = i
        break

if update == -1:
    print(length)
else:
    print(length-update)