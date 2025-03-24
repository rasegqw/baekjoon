import sys

N = int(input())
Anums = set(map(int, sys.stdin.readline().split()))

M = int(input())
Mnums = list(map(int, sys.stdin.readline().split()))

for j in Mnums:
    if j in Anums:  
        print(1)
        Anums.remove(j)
    else:
        print(0)

# remove = []

# for j in Mnums:
#     a = len(Anums)
#     for i in range(a-1, -1, -1):
#         if Anums[i] == j :
#             print(1)
#             Anums.remove(j)
#             remove.append(j)
#             break
#     if a == len(Anums):
#         if j in remove:
#             print(1)
#         else:
#             print(0)


# 결과 출력
# set 사용하면 중복 제거되고, 빠르게 찾을 수 있음.
