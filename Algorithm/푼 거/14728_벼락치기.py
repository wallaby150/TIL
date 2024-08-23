import sys
input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())
tests = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    t, s = tests[i-1]
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]
        if j >= t:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t] + s)

print(dp[-1][-1])
