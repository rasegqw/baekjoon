import sys

M, N, L = map(int, sys.stdin.readline().split())

Mnums = list(map(int, sys.stdin.readline().split()))
Mnums.sort()

count = 0
for i in range(N):
    location = list(map(int, sys.stdin.readline().split()))
    if location[1] > L:
        continue
    else:
        for j in Mnums:
            diff = abs(location[0] - j) if abs(location[0] - j) <= L - location[1] else -1

            if diff != -1:
                count += 1
                break

print(count)