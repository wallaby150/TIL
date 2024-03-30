N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N

for i in range(1, N):
    for j in range(i+1):
        diff = max(nums[j:i + 1]) - min(nums[j:i + 1])
        if j != 0:
            dp[i] = max(dp[i], dp[j-1] + diff)
        else:
            dp[i] = max(dp[i], diff)

print(dp[-1])