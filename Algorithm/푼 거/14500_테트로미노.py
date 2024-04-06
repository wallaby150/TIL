import sys
input = lambda : sys.stdin.readline().rstrip()

# 세로, 가로
N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def dfs(y, x, cnt, score):
    global ans
    if cnt == 4:
        ans = max(ans, score)
        return

    visited[y][x] = 1
    for ty, tx in ((y-1, x), (y, x+1), (y+1, x), (y, x-1)):
        if 0 <= ty < N and 0 <= tx < M and not visited[ty][tx]:
            dfs(ty, tx, cnt + 1, score + nums[ty][tx])
    visited[y][x] = 0
    return


visited = [[0] * M for _ in range(N)]
for Y in range(N):
    for X in range(M):
        # dfs를 통한 4방향 탐색
        dfs(Y, X, 1, nums[Y][X])

        # T미노 확인
        now = nums[Y][X]
        # 세로로 되는지
        if 0 < Y < N-1:
            tmp = nums[Y - 1][X] + nums[Y + 1][X]
            # ㅓ 모양
            if 0 < X:
                ans = max(ans, now + tmp + nums[Y][X-1])
            # ㅏ 모양
            if X < M-1:
                ans = max(ans, now + tmp + nums[Y][X+1])

        # 가로로 되는지
        if 0 < X < M-1:
            tmp = nums[Y][X-1] + nums[Y][X+1]
            # ㅗ 모양
            if 0 < Y:
                ans = max(ans, now + tmp + nums[Y-1][X])
            # ㅜ 모양
            if Y < N-1:
                ans = max(ans, now + tmp + nums[Y+1][X])

print(ans)