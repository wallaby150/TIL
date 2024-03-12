N = int(input())

losses = list(map(int, input().split()))
gains = list(map(int, input().split()))
dp = [0] * 100

for i in range(N):
    for j in range(99, losses[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - losses[i]] + gains[i])

print(dp[99])