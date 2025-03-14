test_case = int(input())

for i in range(test_case):

        AAA = input()
        A = AAA.split(' ')
        total = 0
        num = int(A[0])

        for j in range(1, len(A)):
            A[j] = int(A[j])
            total += A[j]
    
        ave = total/(len(A)-1)
        over_ave =0
        for k in range(1, len(A)):
            if A[k]>ave:
                over_ave +=1
    
        ans = over_ave / (len(A)-1)
        print(f'{round(ans*100, 3)}%')    
