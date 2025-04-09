# N = int(input())
# A = list(map(int, input().split()))

# ans_list = [A[0]]

# for i in range(1, N):
#     for j in range(len(ans_list)):
#         if A[i] <= ans_list[j]:
#             ans_list[j] = A[i]
#             break
#         else:
#             if j == len(ans_list)-1:
#                 ans_list.append(A[i])
#             continue

# print(len(ans_list))


# dp = [1] * N  # 모든 원소는 최소 1개의 부분 수열을 만듦

# for i in range(1, N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))
            # ans_list.append(A[i])


N = int(input())

nums = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

