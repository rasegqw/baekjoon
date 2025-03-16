test_case = int(input())

for i in range(test_case):
    RS = input()
    R = int(RS.split(" ")[0])
    S = RS.split(" ")[1]
    # map
    
    ans = ""

    for j in S:
        ans += j*R

    print(f"{ans}")