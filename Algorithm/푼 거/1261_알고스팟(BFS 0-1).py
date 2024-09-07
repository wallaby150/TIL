import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 0

q = deque([(0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

while q:
    ny, nx = q.popleft()

    if ny == N-1 and nx == M-1:
        print(visited[ny][nx])
        break

    for dy, dx in directions:
        ty, tx = ny + dy, nx + dx
        if 0 <= ty < N and 0 <= tx < M:
            if visited[ty][tx] == -1:
                if grid[ty][tx] == 0:
                    visited[ty][tx] = visited[ny][nx]
                    q.appendleft((ty, tx))
                else:
                    visited[ty][tx] = visited[ny][nx] + 1
                    q.append((ty, tx))
