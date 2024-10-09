import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
highest = [[0] * M for _ in range(N)]
highest[0][0] = 1


def dfs(y, x, passed):
    if len(passed) == 26:
        print(26)
        exit()

    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ty, tx = y + dy, x + dx
        if 0 <= ty < N and 0 <= tx < M:
            if grid[ty][tx] not in passed:
                highest[ty][tx] = max(len(passed) + 1, highest[ty][tx])
                passed.add(grid[ty][tx])
                dfs(ty, tx, passed)
                passed.remove(grid[ty][tx])


dfs(0, 0, set(grid[0][0]))
print(max(max(l) for l in highest))