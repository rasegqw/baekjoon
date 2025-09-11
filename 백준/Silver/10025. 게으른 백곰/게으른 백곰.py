import sys

input = sys.stdin.readline

def solution(N:int, K:int, ices:list):
    ices.sort(key=lambda x:x[1])
    # print(ices)

    left = 0
    max_cnt = 0

    cnt = 0

    for right in range(N):
        cnt += ices[right][0]

        while ices[right][1] - ices[left][1] > 2*K:
            cnt -= ices[left][0]
            left += 1
        
        max_cnt = max(max_cnt, cnt)

    return max_cnt


if __name__=="__main__":
    N, K = map(int, input().split())

    ice_list = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, K, ice_list))