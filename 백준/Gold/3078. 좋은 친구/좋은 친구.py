import sys
import math

input = sys.stdin.readline

def solution(N, K, names:list):

    data = {}
    left = 0
    cnt = 0

    for right in range(N):
        right_l = len(names[right])

        # print(right_l)

        while right - left > K:
            left_l = len(names[left])
            data[left_l] -= 1
            left += 1

        if data.get(right_l) is not None:
            cnt += data[right_l]

        if data.get(right_l) is None:
            data[right_l] = 1
        else:
            data[right_l] += 1

        # print(data)
        # print(cnt)

    return cnt

if __name__=="__main__":

    N, K = map(int, input().split())

    names = [input().strip() for _ in range(N)]

    print(solution(N, K, names))