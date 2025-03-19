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