N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

def can_install(houses, C, dist):
    count = 1
    last = houses[0]

    for i in houses[1::]:
        if i - last >= dist:
            count += 1
            last = i
    return count >= C

def binary_search(houses, C):
    houses.sort()
    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if can_install(houses, C, mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(houses, C))
