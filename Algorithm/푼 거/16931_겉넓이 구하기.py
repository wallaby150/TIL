import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# 위에서는 모두 보이므로 초기값은 N x M * 2
ans = N * M * 2
grid = list([0] + list(map(int, input().split())) + [0] for _ in range(N))
grid = [[0] * (M+2)] + grid + [[0] * (M+2)]

for y in range(1, N+1):
    for x in range(1, M+1):
        cnt = 0
        for ty, tx in [(y-1, x),
                       (y, x+1),
                       (y+1, x),
                       (y, x-1)]:
            cnt += max(grid[y][x] - grid[ty][tx], 0)
        ans += cnt

print(ans)
