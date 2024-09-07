import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 0

q = deque([(0, 0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

while q:
    ny, nx, broke = q.popleft()

    for dy, dx in directions:
        ty, tx = ny + dy, nx + dx

        if 0 <= ty < N and 0 <= tx < M:
            tb = broke + grid[ty][tx]
            # 안 가봤거나, 지금 벽을 부순 게 더 적으면
            if visited[ty][tx] == -1 or tb < visited[ty][tx]:
                visited[ty][tx] = tb
                q.append((ty, tx, tb))

print(visited[-1][-1])
