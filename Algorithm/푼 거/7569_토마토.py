import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

# 가로, 세로, 높이
M, N, H = map(int, input().split())
ans = 10000

grid = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))

on = 0
off = 0
day = 0
q = deque([])
for z in range(H):
    for y in range(N):
        for x in range(M):
            if grid[z][y][x] == 0:
                off += 1
            elif grid[z][y][x] == 1:
                on += 1
                q.append([z, y, x, 0])

while q and off != 0:
    nz, ny, nx, d = q.popleft()
    # 뒤, 오른쪽, 앞, 왼쪽, 위, 아래
    for tz, ty, tx in ((nz, ny+1, nx),
                       (nz, ny, nx+1),
                       (nz, ny-1, nx),
                       (nz, ny, nx-1),
                       (nz-1, ny, nx),
                       (nz+1, ny, nx)):
        if 0 <= tz < H and 0 <= ty < N and 0 <= tx < M:
            if grid[tz][ty][tx] == 0:
                grid[tz][ty][tx] = 1
                on += 1
                off -= 1
                day = d + 1
                q.append([tz, ty, tx, d + 1])



if off == 0:
    print(day)
else:
    print(-1)