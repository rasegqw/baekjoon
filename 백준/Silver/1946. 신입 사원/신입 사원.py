import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 서류 기준으로 정렬
    applicants.sort()

    # 첫 번째 사람은 무조건 채용
    count = 1
    best_interview = applicants[0][1]

    for i in range(1, N):
        # 면접 순위가 더 좋으면 채용
        if applicants[i][1] < best_interview:
            count += 1
            best_interview = applicants[i][1]

    print(count)
