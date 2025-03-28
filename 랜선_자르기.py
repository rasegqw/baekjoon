# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split())

# src = [None] * N

# for i in range(N):
#     src[i] = int(input())

# start = 1
# end = max(src)

# def Check_Val(MID):

#     while True:

#         MID += 1
#         total = 0
#         for i in src:
#             total += i//MID
        
#         if total == K:
#             continue
#         else:
#             return MID-1



# def Binary_Val(ST, EN):
#     if ST == EN:
#         mid = Check_Val(mid)
#         return mid
    
#     mid = (ST + EN)//2
#     total = 0
#     for i in src:
#         total += i//mid

#     if total == K:
#         mid = Check_Val(mid)
#         return mid
    
#     elif total > K:
#         return Binary_Val(mid + 1, EN)
#     else:
#         return Binary_Val(ST, mid)
    

# print(Binary_Val(start, end))

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
