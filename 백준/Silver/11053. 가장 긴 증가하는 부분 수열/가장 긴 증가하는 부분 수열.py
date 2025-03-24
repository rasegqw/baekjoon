N = int(input())
A = list(map(int, input().split()))


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

print(len(ans_list))