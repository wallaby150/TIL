import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cnt, largest = 0, 0


def bfs(sy, sx):
    q = deque([(sy, sx)])
    tmp = 1

    while q:
        ny, nx = q.popleft()
        for ty, tx in [(ny - 1, nx),
                       (ny, nx + 1),
                       (ny + 1, nx),
                       (ny, nx - 1)]:
            if 0 <= ty < N and 0 <= tx < M and grid[ty][tx]:
                grid[ty][tx] = 0
                q.append((ty, tx))
                tmp += 1
    return tmp


for y in range(N):
    for x in range(M):
        if grid[y][x]:
            grid[y][x] = 0
            cnt += 1
            largest = max(largest, bfs(y, x))

print(f'{cnt}\n{largest}')
