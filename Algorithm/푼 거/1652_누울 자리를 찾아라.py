import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [input() for _ in range(N)]
ans = [0, 0]

for i in range(N):
    r, c = 0, 0
    for j in range(N):
        if grid[i][j] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            ans[0] += 1

        if grid[j][i] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            ans[1] += 1

print(*ans)
