import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(int(input()) for _ in range(N))
dp = [[0] * (M+1) for _ in range(N+1)]

for y in range(N):
    num = nums[y]
    for x in range(M+1):
        now = dp[y][x]

        if x != M:
            dp[y+1][x+1] = max(dp[y+1][x+1], now + num)

        # 쉴 때
        if y + max(1, x) <= N:
            dp[y + max(1, x)][0] = max(dp[y + max(1, x)][0], now)

print(dp[N][0])