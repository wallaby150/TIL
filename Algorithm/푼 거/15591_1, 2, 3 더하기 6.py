import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
dp = [1, 1, 2, 2, 3, 3]
for i in range(6, 100001):
    dp.append((dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009)

for _ in range(T):
    N = int(input())
    print(dp[N])
