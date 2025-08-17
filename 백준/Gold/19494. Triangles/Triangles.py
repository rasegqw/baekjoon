import sys
from math import gcd

input = sys.stdin.readline

n, A, B = map(int, input().split())

vertexs = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def find_gcdAngle(dx, dy):
    g = gcd(dx, dy)
    a = dx//g
    b = dy//g

    return (a, b)

for i in range(n):
    vecs = []
    for j in range(n):
        if i == j : continue
        dx = vertexs[j][0] - vertexs[i][0]
        dy = vertexs[j][1] - vertexs[i][1]

        vecs.append((dx, dy))

    counter = {}

    for dx, dy in vecs:
        norm = find_gcdAngle(dx, dy)
        if norm in counter:
            counter[norm].append((dx, dy))
        else:
            counter[norm] = [(dx, dy)]

    for dx, dy in vecs:
        need = find_gcdAngle(-dy, dx)

        if need in counter:
            for i in counter[need]:
                area = (dx*i[1] - dy*i[0])/2
                if A <= area <= B:
                    cnt += 1

print(cnt)