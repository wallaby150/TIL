import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [[100000] * N for _ in range(N)]
ans, cnt = 0, 100000

for x in range(N):
    grid[x][x] = 0

for _ in range(M):
    a, b = map(int, input().split())
    grid[a-1][b-1] = grid[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

for m in range(N):
    now = sum(grid[m])
    if now < cnt:
        ans, cnt = m, now

print(ans + 1)
