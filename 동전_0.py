from collections import deque

N, K = map(int, input().split())

coins = deque()
for _ in range(N):
    coins.appendleft(int(input()))

count = 0

for coin in coins:

    if coin > K:
        continue
    else:
        count += K//coin
        K -= (K//coin) * coin

print(count)