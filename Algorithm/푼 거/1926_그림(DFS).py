import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cnt, largest = 0, 0


def dfs(sy, sx):
        stack = [(sy, sx)]
        grid[sy][sx] = 0
        tmp = 1

        while stack:
            ny, nx = stack.pop()
            for ty, tx in [(ny - 1, nx),
                           (ny, nx + 1),
                           (ny + 1, nx),
                           (ny, nx - 1)]:
                if 0 <= ty < N and 0 <= tx < M and grid[ty][tx]:
                    grid[ty][tx] = 0
                    stack.append((ty, tx))
                    tmp += 1
        return tmp


for y in range(N):
    for x in range(M):
        if grid[y][x]:
            cnt += 1
            largest = max(largest, dfs(y, x))

print(f'{cnt}\n{largest}')
