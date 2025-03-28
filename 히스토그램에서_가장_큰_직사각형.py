import sys
input = sys.stdin.readline

# 본인 높이 * 1 or 이전 높이 * 2 or 최소 높이 * 현재 칸수
while True:
    Num = list(map(int, input().split()))
    for i in range(1, Num[0]+1):
    # 본인 높이 * 1 구하기 (이전 높이보다 높을때만)
        if i==1 or Num[i]>Num[i-1]:
            case1 = Num[i] * 1
            width_count = 1

    # 이전 높이 * 2 구하기 (이전 높이보다 높을 때만)
        if Num[i]>=Num[i-1]:
            height = 0
            width_count += 1
            case2 = height * width_count













# 최소 높이 * 현재 칸수