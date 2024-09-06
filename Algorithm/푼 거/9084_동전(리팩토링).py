import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1

    for i in range(N):
        for j in range(M+1):
            if j >= coins[i]:
                dp[j] += dp[j-coins[i]]

    print(dp[-1])
