import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
# dp[i] = i-1번째 오렌지까지의 최소값
dp = [0, K] + [0] * (N-1)

for i in range(2, N+1):
    high = low = nums[i-1]
    dp[i] = dp[i-1] + K

    # i번째 오렌지의 왼쪽으로 몇 개를 함께 담을 것인지
    for j in range(1, min(i, M)):
        k = i - j - 1
        high = max(high, nums[k])
        low = min(low, nums[k])
        dp[i] = min(dp[i], dp[k] + (j + 1) * (high - low) + K)

print(dp[-1])
