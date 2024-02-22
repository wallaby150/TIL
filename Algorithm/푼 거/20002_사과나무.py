import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
grid = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        grid[i][j] = grid[i][j - 1] + grid[i - 1][j] - grid[i - 1][j - 1] + nums[i - 1][j - 1]

ans = grid[1][1]
for y in range(1, N + 1):
    for x in range(1, N + 1):
        for k in range(N):
            if y + k == N + 1 or x + k == N + 1:
                break

            tmp = grid[y+k][x+k] - grid[y-1][x+k] - grid[y+k][x-1] + grid[y-1][x-1]
            ans = max(tmp, ans)

print(ans)