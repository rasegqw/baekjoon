import sys

N = int(input())

stack = [None] * N

for i in range(N):
    stack[i] = int(sys.stdin.readline())

pivot_num = stack[-1]
count = 1
while len(stack) != 0:
    a = stack.pop()
    if a>pivot_num :
        pivot_num = a
        count += 1
    

print(count)