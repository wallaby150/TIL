import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# BFS를 실행하여 가장 먼 거리를 구하는 함수
def bfs(y, x):
    q = deque([(y, x, 0)])  # (y좌표, x좌표, 거리)
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    farthest_point = (y, x, 0)  # (y좌표, x좌표, 최대거리)

    while q:
        ny, nx, cnt = q.popleft()
        farthest_point = (ny, nx, cnt)

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ty, tx = ny + dy, nx + dx
            if 0 <= ty < N and 0 <= tx < M and grid[ty][tx] == 'L' and not visited[ty][tx]:
                visited[ty][tx] = True
                q.append((ty, tx, cnt + 1))

    return farthest_point

# 첫 번째 BFS로 임의의 육지에서 가장 먼 점 찾기
max_distance = 0
for Y in range(N):
    for X in range(M):
        if grid[Y][X] == 'L':
            # 첫 번째 육지에서 가장 먼 점 찾기
            farthest_y, farthest_x, _ = bfs(Y, X)
            # 그 점에서 다시 BFS를 해서 가장 먼 거리를 구함
            _, _, distance = bfs(farthest_y, farthest_x)
            max_distance = max(max_distance, distance)

print(max_distance)
