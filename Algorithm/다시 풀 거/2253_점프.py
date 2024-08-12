import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
high = int((2 * N) ** 0.5) + 1

dp = [[10001] * (high + 1) for _ in range(N + 1)]
dp[1][0] = 0
empty = set(int(input()) for _ in range(M))

for i in range(2, N + 1):
    if i in empty:
        continue

    for j in range(high):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == 10001:
    print(-1)
else:
    print(min(dp[N]))

