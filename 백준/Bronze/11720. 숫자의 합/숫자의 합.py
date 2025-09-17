import sys

input = sys.stdin.readline

N = int(input())

x = input().strip()

sum_all = 0

for i in x:
    # print(i)
    sum_all += int(i)

print(sum_all)