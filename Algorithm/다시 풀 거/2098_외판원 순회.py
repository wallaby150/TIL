import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
dp = [[-1] * (1 << N) for _ in range(N)]


def dfs(now, visited):
    if visited == (1 << N) - 1:
        if grid[now][0]:
            return grid[now][0]
        return INF

    if dp[now][visited] != -1:
        return dp[now][visited]

    dp[now][visited] = INF

    for i in range(1, N):
        if not visited & (1 << i) and grid[now][i]:
            dp[now][visited] = min(dp[now][visited], dfs(i, visited | (1 << i)) + grid[now][i])

    return dp[now][visited]


print(dfs(0, 1))
