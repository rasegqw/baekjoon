# N, M = map(int, input().split())

# Ntree = list(map(int, input().split()))

# def findH(n, sumH, h):

#     if Ntree[n] - h <= 0:
#         n += 1
#     else:
#         sumH += Ntree[n] - h
#         n += 1

#     if sumH <= M and n < N :
#         x = findH(n, sumH, h)
#     elif sumH == M and n == N:
#         return h
#     else:
#         return 0
#     return x

# x = 0
# real = 0 
# height=0
# while x == 0 :
#     height += 1
#     x = findH(0, real, height)

# print(x)

N, M = map(int, input().split())
Ntree = list(map(int, input().split()))

start = 0
end = max(Ntree)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum((tree - mid) for tree in Ntree if tree > mid)
    
    if total >= M:
        result = mid  # 더 높이 잘라도 되니 저장하고 오른쪽으로 이동
        start = mid + 1
    else:
        end = mid - 1

print(result)