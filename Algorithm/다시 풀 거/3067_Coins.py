import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(N):
        for j in range(coins[i], target + 1):
            dp[j] += dp[j - coins[i]]
    
    print(dp[target])