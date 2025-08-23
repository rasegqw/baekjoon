import sys
import math

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B, X = map(int, input().split())

    if A%B == 0:
        print(X//B)
    else:
        res = 0
        x = math.gcd(A, B)
        
        res += (X)//x
            
        print(res)