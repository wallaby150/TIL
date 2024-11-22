n, m = map(int, input().split())

grid = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m // 2):
        if grid[i][m - j - 1] == '.':
            grid[i][m - j - 1] = grid[i][j]
        elif grid[i][j] == '.':
            grid[i][j] = grid[i][m - j - 1]

for row in grid:
    print(''.join(row))
