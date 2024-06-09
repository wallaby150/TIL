import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for y in range(1, N+1):
    for x in range(1, K+1):
        if x < bags[y-1][0]:
            dp[y][x] = dp[y-1][x]
        else:
            dp[y][x] = max(dp[y-1][x], bags[y-1][1] + dp[y-1][x-bags[y-1][0]])

print(dp[N][K])
