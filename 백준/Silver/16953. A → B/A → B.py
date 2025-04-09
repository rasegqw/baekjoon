import heapq

A, B = map(int, input().split())

que = [(1, A)]
count = -1

while que:
    now, now_num = heapq.heappop(que)

    if now_num > B:
        continue
    if now_num == B:
        count = now
        break

    heapq.heappush(que, (now+1, now_num*10+1))
    heapq.heappush(que, (now+1, now_num*2))

print(count)