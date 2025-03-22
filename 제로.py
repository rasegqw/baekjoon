import sys

K = int(input())

stack = []

for i in range(K):
    a = int(sys.stdin.readline())
    if a != 0:
        stack.append(a)
    else:
        stack.pop()
total = 0
for i in stack:
    total += i

print(total)