import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
INF = 10 ** 8
grid = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [INF, []]

for _ in range(M):
    a, b, t = map(int, input().split())
    grid[a][b] = t

for x in range(N + 1):
    grid[x][x] = 0

K = int(input())
dots = list(map(int, input().split()))

# 플로이드 워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if grid[i][j] > grid[i][k] + grid[k][j]:
                grid[i][j] = grid[i][k] + grid[k][j]

for p in range(1, N+1):
    tmp = 0
    for dot in dots:
        tmp = max(tmp, grid[p][dot] + grid[dot][p])
        if tmp > ans[0]:
            break

    if tmp == ans[0]:
        ans[1].append(p)
    elif tmp < ans[0]:
        ans[0] = tmp
        ans[1] = [p]

print(*ans[1])
