import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
visited = [[False] * M for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
ans = 0


def dfs(y, x):
    stack = [(y, x)]
    visited[y][x] = True

    while stack:
        ny, nx = stack.pop()
        for dy, dx in direction:
            ty, tx = ny + dy, nx + dx
            if 0 <= ty < N and 0 <= tx < M and not visited[ty][tx] and grid[ty][tx]:
                stack.append((ty, tx))
                visited[ty][tx] = True
    return


for i in range(N):
    for j in range(M):
        if grid[i][j] and not visited[i][j]:
            ans += 1
            dfs(i, j)
print(ans)
