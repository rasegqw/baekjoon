# import sys

# input = sys.stdin.readline

# N = int(input())
# dot = []

# for _ in range(N):
#     a, b = map(int, input().split())
#     dot.append([a, b])

# min_width = float('inf')

# for i in range(N):
#     for j in range(i + 1, N):        
#         width = (dot[i][0] - dot[j][0])**2 + (dot[i][1] - dot[j][1])**2
#         min_width = min(min_width, width)

# print(int(min_width))


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def brute_force(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if points[i] == points[j]:
                return 0
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def closest_pair(points_x, points_y):
    n = len(points_x)
    if n <= 3:
        return brute_force(points_x)
    
    mid = n // 2
    mid_x = points_x[mid][0]            # 얘는 Left와 Right의 점들간의 거리 체크해주는 놈
    
    left_x = points_x[:mid]
    right_x = points_x[mid:]

    # 좌우 Y 분할 수정
    left_y = []
    right_y = []
    left_set = set(left_x)  # 이거 왜하는거임?
    for p in points_y:
        if p in left_set:
            left_y.append(p)
        else:
            right_y.append(p)

    left_min = closest_pair(left_x, left_y)
    right_min = closest_pair(right_x, right_y)
    d = min(left_min, right_min)

    # Strip 구성
    strip = [p for p in points_y if abs(p[0] - mid_x) ** 2 < d]

    # 최소 거리 계산
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):              # 여기서 i+7이 의미하는 바는, 최대 6개만 비교해봐도 된대(Packing density)
            if strip[i] == strip[j]:
                return 0
            d = min(d, distance(strip[i], strip[j]))

    return d

# 입력 처리
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points_x = sorted(points)
points_y = sorted(points, key=lambda p: p[1])

print(closest_pair(points_x, points_y))
