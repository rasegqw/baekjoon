T = int(input())


for i in range(T):
    N = int(input())

    if (N == 0):
        print("1 0")

    elif (N == 1):
        print("0 1")
    else:
        dp0 = [0] * (N+1)
        dp1 = [0] * (N+1)

        dp0[0] = 1
        dp1[1] = 1
        
        dp0[2] = 1
        dp1[2] = 1

        for j in range(3, N+1):
            dp1[j] = dp1[j-1] + dp1[j-2]
            dp0[j] = dp0[j-1] + dp0[j-2]

        print(dp0[N], dp1[N])