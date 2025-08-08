import sys

input = sys.stdin.readline
N = int(input())

City = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')  # 최소 비용 저장 변수
visited = [False] * N  # 방문한 도시 체크

def tsp(cur_city, count, total_cost, start_city):
    global min_cost

    if count == N:  # 모든 도시 방문 완료
        if City[cur_city][start_city] != 0:  # 시작점으로 돌아갈 수 있는 경우
            min_cost = min(min_cost, total_cost + City[cur_city][start_city])
        return

    for next_city in range(N):
        if not visited[next_city] and City[cur_city][next_city] != 0:
            visited[next_city] = True
            tsp(next_city, count + 1, total_cost + City[cur_city][next_city], start_city)
            visited[next_city] = False  # 백트래킹

# 모든 도시에서 출발하는 경우를 고려
for start in range(N):
    visited[start] = True
    tsp(start, 1, 0, start)
    visited[start] = False  # 다음 출발점 고려

print(min_cost)