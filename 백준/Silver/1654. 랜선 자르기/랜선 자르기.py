import sys
input = sys.stdin.readline

K, N = map(int, input().split())
src = [int(input()) for _ in range(K)]

start = 1
end = max(src)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(i // mid for i in src)

    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
