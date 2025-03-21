import sys

N = int(input())
Anums = set(map(int, sys.stdin.readline().split()))

M = int(input())
Mnums = list(map(int, sys.stdin.readline().split()))

for j in Mnums:
    if j in Anums:  
        print(1)
    else:
        print(0)