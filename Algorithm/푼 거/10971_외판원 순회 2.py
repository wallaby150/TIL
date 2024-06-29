import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 10 ** 8
visited = [0] * N


def dfs(start, now, cnt, cost):
    global ans

    if cost > ans:
        return

    if cnt == N:
        if grid[now][start]:
            ans = min(ans, cost + grid[now][start])
        return

    for j in range(N):
        # 안 가봤고, 길이 있다면
        if not visited[j] and grid[now][j]:
            visited[j] = 1
            dfs(start, j, cnt+1, cost+grid[now][j])
            visited[j] = 0


for i in range(N):
    visited[i] = 1
    dfs(i, i, 1, 0)
    visited[i] = 0

print(ans)
