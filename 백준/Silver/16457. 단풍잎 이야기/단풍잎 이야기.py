import sys
from itertools import combinations

input = sys.stdin.readline

# def solution(v):

#     return

if __name__ == "__main__":
    # n: 키 개수, m: 퀘스트 개수, k: 퀘스트당 사용해야하는 스킬 수
    n, m, k = map(int, input().split())

    quests = []

    for _ in range(m):
        q_num = set(map(int, input().split()))
        
        quests.append(q_num)

    # print(quests)

    cnt = 0

    # quests의 원소인 quest 집합을 부분집합으로 갖는
    # 1부터 2n까지 숫자 중, n개만큼 가지고 있는 res 집합을 만들어서
    # quest 집합을 부분집합으로 가장 많이 가질 수 있는
    # res 집합의 quest 집합 수.
    # 를 구하는 법.

    for comb in combinations(range(1, 2*n+1), n):
        res = set(comb)
        count = 0

        for q in quests:
            q: set[int]
            if q.issubset(res):
                count+=1

        cnt = max(cnt, count)

    print(cnt)