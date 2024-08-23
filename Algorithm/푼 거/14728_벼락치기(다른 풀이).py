import sys
input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())
tests = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (T+1)

for n in range(N):
    t, s = tests[n]
    for i in range(T, t - 1, -1):
        dp[i] = max(dp[i], dp[i - t] + s)

print(dp[-1])
