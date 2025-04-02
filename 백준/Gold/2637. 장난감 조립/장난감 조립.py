from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

Toy = defaultdict(list)  # 제품 조립에 필요한 부품 정보 저장
in_degree = [0] * (N+1)  # 진입 차수 저장
needs = [defaultdict(int) for _ in range(N+1)]  # 필요한 기본 부품 개수 저장

for _ in range(M):
    x, y, k = map(int, input().split())
    Toy[y].append((x, k))
    in_degree[x] += 1  # 진입 차수 증가

queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:  # 진입 차수가 0이면 기본 부품
        queue.append(i)

needs[N][N] = 1  # 최종 제품 1개 필요

while queue:
    now = queue.popleft()
    
    for next_part, count in Toy[now]:
        if not needs[now]:  # 기본 부품이면
            needs[next_part][now] += count
        else:  # 중간 부품이면 기본 부품 개수 누적
            for key, val in needs[now].items():
                needs[next_part][key] += val * count
        
        in_degree[next_part] -= 1
        if in_degree[next_part] == 0:
            queue.append(next_part)

for part in sorted(needs[N].keys())[:-1:]:
    print(part, needs[N][part])
