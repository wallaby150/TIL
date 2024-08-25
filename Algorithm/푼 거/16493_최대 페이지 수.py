import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dp = [0] * (N + 1)

for _ in range(M):
    day, paper = map(int, input().split())
    for i in range(N, day-1, -1):
        dp[i] = max(dp[i], dp[i-day] + paper)

print(dp[-1])
