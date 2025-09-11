import sys

input = sys.stdin.readline

IS_PEAK = lambda x : x <= 138 and x >= 129

def solution(N:int, L:int, alchols:list):
    
    cnt = 0
    max_t = 0
    t = 0

    for i in range(N):
        cnt += alchols[i]
        if i-L >= 0:
            cnt -= alchols[i-L]
        
        if IS_PEAK(cnt):
            t += 1
            max_t = max(max_t, t)
        # else:
        #     t = 0
        
        # print(t, cnt)

    return max_t

if __name__=="__main__":

    N, L = map(int, input().split())

    alchols = list(map(int, input().split()))

    print(solution(N, L, alchols))