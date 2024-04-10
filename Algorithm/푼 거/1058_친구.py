import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
grid = list(list(input()) for _ in range(N))
f = list([0] * N for _ in range(N))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if grid[i][j] == 'Y' or grid[i][k] == grid[k][j] == 'Y':
                f[i][j] = 1

ans = 0
for line in f:
    ans = max(ans, sum(line))
print(ans)