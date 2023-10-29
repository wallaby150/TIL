N = int(input())
coins = [7, 5, 2]
dp = [num for num in range(N+10)]
dp[0] = 0

for i in range(N+1):
    for coin in coins:
        dp[i+coin] = min(dp[i] + 1, dp[i+coin])

print(dp[N])