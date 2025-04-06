N = int(input())

schedule = []

for _ in range(N):
    start, end = map(int, input().split())
    schedule.append([end, start])

schedule.sort()

count = 0
now_end = 0

for end, start in schedule:
    if start >= now_end:
        now_end = end
        count += 1
    
print(count)