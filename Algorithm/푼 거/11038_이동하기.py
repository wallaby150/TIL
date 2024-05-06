import sys
input = lambda: sys.stdin.readline().rstrip()

# 세로 N, 가로 M
N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))

for y in range(N):
    for x in range(M):
        tmp1 = grid[y-1][x] if 0 < y else 0
        tmp2 = grid[y][x-1] if 0 < x else 0
        grid[y][x] = grid[y][x] + max(tmp1, tmp2)

print(grid[N-1][M-1])
