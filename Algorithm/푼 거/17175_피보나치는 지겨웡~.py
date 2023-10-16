import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
count = 2
dp = [1, 1]

if n < 2:
    print(dp[n])
else:
    for _ in range(n-1):
        dp.append(dp[-1] + dp[-2]+1)
    print(dp[-1] % 1000000007)