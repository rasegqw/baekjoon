# import sys

# N, C = map(int, input().split)

# dir = [None] * N
# for i in range(N):
#     dir[i] = sys.stdin.readline()


# # 만약 두개 -> 처음과 끝
# # 세개면? 처음과 끝의 중간값과 가장 가까운 놈
# # 네개면? 처음과 끝과 

# # if N == C:


# dir.sort()
# a = (dir[N-1]) + min(dir[0])//2

# # for i in range(a):
# visited = []

# def findMid(mini, maxi):
#     global dir
#     if (mini+maxi)//2 in dir:
#         visited.append(dir.index[(mini+maxi)//2])
#         count += 1
#     else:






# N, M = map(int, input().split())
# Ntree = list(map(int, input().split()))

# start = 0
# end = max(Ntree)
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     total = sum((tree - mid) for tree in Ntree if tree > mid)
    
#     if total >= M:
#         result = mid  # 더 높이 잘라도 되니 저장하고 오른쪽으로 이동
#         start = mid + 1
#     else:
#         end = mid - 1

# print(result)


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

def can_install(houses, C, dist):
    count = 1
    last = houses[0]

    for i in houses[1::]:
        if i - last >= dist:
            count += 1
            last = i
    return count >= C

def binary_search(houses, C):
    houses.sort()
    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if can_install(houses, C, mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(houses, C))
