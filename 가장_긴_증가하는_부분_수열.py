# import sys

# N = int(input())

# Anums = list(map(int, sys.stdin.readline().split()))

# pivot_num = Anums[0]
# d_pivot_num = Anums[0]
# count = 1
# d_count = 1

# for i in range(1, N):
#     if Anums[i] > pivot_num:
#         count += 1
#         pivot_num = Anums[i]

#     if Anums[i] > d_pivot_num:
#         d_count += 1
#         d_pivot_num = Anums[i]
#         if d_count>count :
#             count = d_count
#             pivot_num = d_pivot_num
#     elif Anums[i] == d_pivot_num :
#         continue
#     else:
#         d_count = 1
#         d_pivot_num = Anums[i]



# print(count)

N = int(input())
A = list(map(int, input().split()))

# dp = [1] * N  # 모든 원소는 최소 1개의 부분 수열을 만듦

# for i in range(1, N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

ans_list = [A[0]]

for i in range(1, N):
    for j in range(len(ans_list)):
        if A[i] <= ans_list[j]:
            ans_list[j] = A[i]
            break
        else:
            if j == len(ans_list)-1:
                ans_list.append(A[i])
            continue
            # ans_list.append(A[i])

print(len(ans_list))