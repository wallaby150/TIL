import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stones = list(map(int, input().split()))
dp = [5000 * 1000000] * N
dp[0] = 0


for i in range(1, N):
    for j in range(i):
        tmp = (i - j) * (1 + abs(stones[i] - stones[j]))
        dp[i] = min(dp[i], max(tmp, dp[j]))

print(dp[-1])
