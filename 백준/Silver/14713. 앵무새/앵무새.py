import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

parrot = [deque(input().strip().split()) for _ in range(N)]

sentence = deque(map(str, input().strip().split()))

for word in sentence:
    check = False

    for i in range(N):
        if parrot[i] and word == parrot[i][0]:
            parrot[i].popleft()
            check = True
            break            

    if not check:
        print("Impossible")
        sys.exit(0)


if all(not i for i in parrot):
    print("Possible")
else:
    print("Impossible")