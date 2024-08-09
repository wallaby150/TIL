import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
sheep, wolf = 0, 0

for y in range(N):
    for x in range(M):
        if grid[y][x] != '#':
            q = deque([(y, x)])
            now = {'o': 0, 'v': 0, '.': 0}
            now[grid[y][x]] += 1
            grid[y][x] = '#'

            while q:
                ny, nx = q.popleft()
                for ty, tx in [(ny-1, nx),
                               (ny, nx+1),
                               (ny+1, nx),
                               (ny, nx-1)]:
                    if 0 <= ty < N and 0 <= tx < M and grid[ty][tx] != '#':
                        now[grid[ty][tx]] += 1
                        grid[ty][tx] = '#'
                        q.append((ty, tx))

            if now['o'] > now['v']:
                sheep += now['o']
            else:
                wolf += now['v']

print(sheep, wolf)
