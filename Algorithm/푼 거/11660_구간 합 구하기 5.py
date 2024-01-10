import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

grid = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        grid[i][j] = grid[i][j - 1] + grid[i - 1][j] - grid[i - 1][j - 1] + nums[i - 1][j - 1]

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = grid[x2][y2] - grid[x2][y1 - 1] - grid[x1 - 1][y2] + grid[x1 - 1][y1 - 1]
    print(result)
