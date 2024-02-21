import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
# 최대값, 최소값
dp = [[[-626, 3126] for _ in range(N)] for _ in range(N)]
greed = list(list(input().split()) for _ in range(N))
first = int(greed[0][0])


def solve(y, x, num):
    if dp[y][x][1] <= num <= dp[y][x][0]:
        return
    else:
        dp[y][x][0] = max(dp[y][x][0], num)
        dp[y][x][1] = min(dp[y][x][1], num)

    if y == x == N-1:
        return

    if x + 2 < N:
        tmp1 = eval(str(num) + greed[y][x+1] + greed[y][x+2])
        solve(y, x+2, tmp1)

    if y + 1 < N and x + 1 < N:
        tmp2 = eval(str(num) + greed[y][x+1] + greed[y+1][x+1])
        solve(y+1, x+1, tmp2)
        tmp3 = eval(str(num) + greed[y+1][x] + greed[y+1][x+1])
        solve(y+1, x+1, tmp3)

    if y + 2 < N:
        tmp4 = eval(str(num) + greed[y+1][x] + greed[y+2][x])
        solve(y+2, x, tmp4)


solve(0, 0, first)
print(*dp[N-1][N-1])