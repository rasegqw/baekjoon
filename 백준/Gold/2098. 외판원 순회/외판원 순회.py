import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(current, visited):
    if visited == (1 << N) - 1:
        return W[current][0] if W[current][0] > 0 else INF

    if dp[current][visited] != -1:
        return dp[current][visited]

    min_cost = INF
    for next_city in range(N):
        if not (visited & (1 << next_city)) and W[current][next_city] != 0:
            cost = W[current][next_city] + tsp(next_city, visited | (1 << next_city))
            min_cost = min(min_cost, cost)

    dp[current][visited] = min_cost
    return min_cost

print(tsp(0, 1))  # 0번 도시에서 시작, 0번은 방문한 상태
