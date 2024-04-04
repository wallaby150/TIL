import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(float(input()) for _ in range(N))
dp = nums[:]

for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1] * dp[i])

print(f'{max(dp):0.3f}')