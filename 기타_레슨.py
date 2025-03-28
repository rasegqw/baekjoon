import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Lecs = list(map(int, input().split()))

start = max(Lecs)
end = sum(Lecs)
# res = []

def check(Mid):
    count = 1
    total = 0
    # total_max = 0
    for i in Lecs:
        if total + i > Mid:
            count += 1
            # total_max = max(total_max, total)
            total = i

        else:
            total += i

    # count += 1   # 마지막 강의들이 들어가는 블루레이

    # total_max = max(total_max, total)

    # if count <= M:
    #     res.append(total_max)
    
    return count <= M


while start <= end:
    mid = (start + end)//2
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)