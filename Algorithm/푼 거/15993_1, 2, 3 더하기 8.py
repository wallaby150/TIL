T = int(input())
dp = [[0, 0], [1, 0], [1, 1], [2, 2], [3, 4]]

for _ in range(T):
    N = int(input())

    if N >= len(dp):
        for i in range(len(dp), N+1):
            odd = (dp[i-3][0] + dp[i-2][0] + dp[i-1][0]) % 1000000009
            even = (dp[i-3][1] + dp[i-2][1] + dp[i-1][1]) % 1000000009
            dp.append([even, odd])

    print(*dp[N])
