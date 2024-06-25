import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# 위에서는 모두 보이므로 초기값은 N x M * 2
ans = N * M
grid = list(list(map(int, input().split())) for _ in range(N))

for y in range(N):
    for x in range(M):
        if x == 0:
            ans += grid[y][x]
        else:
            ans += max(grid[y][x] - grid[y][x-1], 0)

for x in range(M):
    for y in range(N):
        if y == 0:
            ans += grid[y][x]
        else:
            ans += max(grid[y][x] - grid[y-1][x], 0)

print(ans * 2)
