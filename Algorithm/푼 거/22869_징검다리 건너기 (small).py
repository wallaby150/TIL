import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for i in range(N - 1):
    if dp[i] == 1:
        for j in range(i + 1, N):
            if dp[j] == 0 and K >= (j - i) * (1 + abs(nums[i] - nums[j])):
                dp[j] = 1

if dp[N - 1] == 1:
    print('YES')
else:
    print('NO')
