import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
ans = 0


def bfs(y, x):
    q = deque([(y, x, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    high = 0

    while q:
        ny, nx, cnt = q.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ty, tx = ny + dy, nx + dx
            if 0 <= ty < N and 0 <= tx < M and grid[ty][tx] == 'L' and visited[ty][tx] == False:
                visited[ty][tx] = True
                q.append((ty, tx, cnt + 1))
                high = max(cnt + 1, high)

    return high


for Y in range(N):
    for X in range(M):
        if grid[Y][X] == 'L':
            ans = max(bfs(Y, X), ans)

print(ans)