N, M = map(int, input().split())
Ntree = list(map(int, input().split()))

start = 0
end = max(Ntree)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum((tree - mid) for tree in Ntree if tree > mid)
    
    if total >= M:
        result = mid 
        start = mid + 1
    else:
        end = mid - 1

print(result)