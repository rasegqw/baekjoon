import sys
from collections import deque

N = int(sys.stdin.readline().strip())
Land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_area = 0  # 최대 영역 개수 저장

# BFS 탐색 함수
def bfs(x, y, k, visited):
    queue = deque([(x, y)])
    visited.add((x, y))  # 방문 처리
    
    # 네 방향 이동 (위, 아래, 왼쪽, 오른쪽)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # 인덱스 범위 확인 & 방문 여부 확인 & 기준 높이보다 높은 곳만 탐색
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and Land[nx][ny] > k:
                visited.add((nx, ny))  # 방문 처리
                queue.append((nx, ny))

# 가능한 모든 k값에 대해 실행
for k in range(max(map(max, Land))):  # Land 내 최댓값까지만 검사
    count = 0  # 현재 높이 k에서의 영역 개수 초기화
    visited = set()  # 방문한 좌표 저장 (중복 방지)

    for i in range(N):
        for j in range(N):
            if Land[i][j] > k and (i, j) not in visited:
                bfs(i, j, k, visited)  # BFS 실행
                count += 1  # 새로운 영역 발견

    max_area = max(max_area, count)  # 최대 영역 개수 갱신

print(max_area)

