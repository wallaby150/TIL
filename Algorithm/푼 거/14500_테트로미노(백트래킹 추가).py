import sys
input = lambda : sys.stdin.readline().rstrip()

# 세로, 가로
N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
ans = 0
high = max(map(max, nums))


def dfs(y, x, cnt, score):
    global ans
    if score + (4 - cnt) * high < ans:
        return

    if cnt == 4:
        ans = max(ans, score)
        return

    for ty, tx in ((y-1, x), (y, x+1), (y+1, x), (y, x-1)):
        if 0 <= ty < N and 0 <= tx < M and not visited[ty][tx]:
            visited[ty][tx] = 1
            if cnt == 2:
                dfs(y, x, cnt + 1, score + nums[ty][tx])
            dfs(ty, tx, cnt + 1, score + nums[ty][tx])
            visited[ty][tx] = 0
    return


visited = [[0] * M for _ in range(N)]
for Y in range(N):
    for X in range(M):
        visited[Y][X] = 1
        # dfs를 통한 4방향 탐색
        dfs(Y, X, 1, nums[Y][X])
        visited[Y][X] = 0

print(ans)