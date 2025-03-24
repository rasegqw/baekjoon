import heapq
import sys

# N = 사람 수
# H = 사람들 집, 회사 배열
# D = 철로 길이

N = int(input())
H = [None] * N

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    H[i] = sorted(a)

heapq.heapify(H)
D = int(input())

val_count = 0

for i in range(N):
    if i>0 and H[i][0] == H[i-1][0] :
        continue
    else:
        start = H[i][0]
        count = 0
        x = True

        while x:
            for j in range(i, N):
                if D - H[j][1] + start >= 0 :
                    count += 1
                    x = True
                    if j == N-1:
                        x = False
                else:
                    x = False
                    break
        val_count = max(val_count, count)

print(val_count)


heapq.heappop()