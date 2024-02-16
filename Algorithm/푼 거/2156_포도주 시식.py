import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(int(input()) for _ in range(N))
dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(N):
    dp[i+1][0] = max(dp[i])
    dp[i+1][1] = dp[i][0] + nums[i]
    dp[i+1][2] = dp[i][1] + nums[i]

print(max(dp[-1]))