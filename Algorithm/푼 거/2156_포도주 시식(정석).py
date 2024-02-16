import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [0] * N
nums = list(int(input()) for _ in range(N))
dp = [0] * N

dp[0] = nums[0]
if N > 1:
    dp[1] = nums[0] + nums[1]
if N > 2:
    dp[2] = max(nums[2] + nums[1], nums[2] + nums[0], dp[1])
for j in range(3, N):
    dp[j] = max(nums[j] + dp[j - 2],
                nums[j] + nums[j - 1] + dp[j - 3],
                dp[j - 1])

print(max(dp))