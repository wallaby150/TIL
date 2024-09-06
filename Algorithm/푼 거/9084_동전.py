import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    M = int(input())
    dp = [[0] * (M+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, len(coins)):
        for j in range(M+1):
            dp[i][j] = dp[i-1][j]
            if j >= coins[i]:
                dp[i][j] += dp[i][j-coins[i]]

    print(dp[-1][-1])
