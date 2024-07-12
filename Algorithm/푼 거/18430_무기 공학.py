import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0


def dfs(y, x, now):
    global ans

    if x == M:
        y += 1
        x = 0

    if y == N:
        ans = max(ans, now)
        return

    if not visited[y][x]:
        for ty1, tx1, ty2, tx2 in [(y, x - 1, y - 1, x),
                                   (y - 1, x, y, x + 1),
                                   (y, x + 1, y + 1, x),
                                   (y + 1, x, y, x - 1)]:
            if 0 <= ty1 < N and 0 <= ty2 < N and 0 <= tx1 < M and 0 <= tx2 < M:
                if not visited[ty1][tx1] and not visited[ty2][tx2]:
                    visited[y][x] = visited[ty1][tx1] = visited[ty2][tx2] = True
                    dfs(y, x + 1, now + nums[y][x] * 2 + nums[ty1][tx1] + nums[ty2][tx2])
                    visited[y][x] = visited[ty1][tx1] = visited[ty2][tx2] = False

    dfs(y, x+1, now)
    return


dfs(0, 0, 0)
print(ans)
