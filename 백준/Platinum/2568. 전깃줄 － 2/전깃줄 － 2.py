import sys
import bisect

input = sys.stdin.readline


def solution(lines):
    
    sorted_lines = sorted(lines.items(), key=lambda x: x[0])
    values = [b for a, b in sorted_lines]

    # LIS를 구하고, 실제 LIS 원소 추적
    LIS = []
    positions = []

    for v in values:
        idx = bisect.bisect_left(LIS, v)
#        print(v, idx)
        if idx == len(LIS):
            LIS.append(v)
        else:
            LIS[idx] = v
#        print("LIS ", LIS)
        positions.append(idx)


#    print("positions ", positions)
    
    
    # for key in v:
    #     A.add(key)
    #     B.add(v[key])

    # for key, value in v.items():
    #     A.add(key)
    #     B.add(value)

    lis_length = len(LIS)
    lis_set = set()
    current_idx = lis_length - 1
    for i in range(len(positions)-1, -1, -1):
        if positions[i] == current_idx:
            lis_set.add(sorted_lines[i][0])
            current_idx -= 1

    res = [a for a, b in sorted_lines if a not in lis_set]
    return res


if __name__=="__main__":
    N = int(input())

    lines = {}
    for _ in range(N):
        line = list(map(int, input().split()))
        lines[line[0]] = line[1]

    result = solution(lines)

    print(len(result))
    for i in result:
        print(i)
