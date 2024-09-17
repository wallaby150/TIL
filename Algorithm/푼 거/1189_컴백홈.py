import sys
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
grid = [list(input()) for _ in range(N)]
grid[N-1][0] = 1


def dfs(y, x, cnt):
    if cnt > K:
        return 0

    if y == 0 and x == M - 1:
        if cnt == K:
            return 1
        return 0

    now = 0

    for ty, tx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
        if 0 <= ty < N and 0 <= tx < M and grid[ty][tx] == '.':
            grid[ty][tx] = cnt + 1
            now += dfs(ty, tx, cnt + 1)
            grid[ty][tx] = '.'

    return now


ans = dfs(N-1, 0, 1)
print(ans)