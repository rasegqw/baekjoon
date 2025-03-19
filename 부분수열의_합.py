# N, S = map(int, input().split())
# num = list(map(int, input().split()))

# SUMNUM = sum(num)
# def findSum(a, sum, number = 1, index = 0 ):
#     # if number == 1:
#     #     for i in range(len(a)):
#     #         if a[i] == sum :
#     #             count +=1
#     #     if len(num) == number:
#     #         return count
#     #     findSum(a, sum, number+1, index)
#     # else:
#         x = [None] * number

#         for i in range(index, number):
#             x[i] = a[]

#             if sum(x) == sum:
#                 count += 1
#             if len(num) == number:
#                 return count
#             findSum(a, sum, number+1, index)


N, S = map(int, input().split())  # 정수 개수 N, 목표 합 S 입력
num = list(map(int, input().split()))  # 수열 입력

count = 0

for bit in range(1, 1<<N):
    sum_part = 0
    for i in range(N):
        if bit & (1<<i):
            sum_part += num[i]
    
    if sum_part == S :
        count +=1


print(count)

















# count = 0  # S가 되는 부분수열 개수

# # 모든 부분집합 탐색 (비트마스크 사용)
# for bit in range(1, 1 << N):  # 1부터 (2^N - 1)까지 탐색
# # 1 << N : 1을 왼쪽으로 N 만큼 이동시키는 연산.

#     subset_sum = 0  # 현재 부분집합의 합
#     for i in range(N):
#         if bit & (1 << i):  # i번째 원소가 부분집합에 포함된 경우
#             subset_sum += num[i]

#     if subset_sum == S:  # 부분집합의 합이 S와 같다면 카운트 증가
#         count += 1

# print(count)  # 결과 출력
