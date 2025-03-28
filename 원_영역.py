import sys
input = sys.stdin.readline

N = int(input())

circles = []

for i in range(N):
    a, b = map(int, input().split())
    circles.append(a, b)


circles.sort()

draw = []

for i in circles:
    dot1 = i[0] - i[1]
    dot2 = i[0] + i[1]

    if dot1 in draw:
        