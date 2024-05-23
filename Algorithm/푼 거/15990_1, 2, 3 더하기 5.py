import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
dp = [[0,0,0], [1,0,0], [0,1,0], [1,1,1]]

for _ in range(T):
    N = int(input())

    for i in range(len(dp), N+1):
        tmp = []
        tmp.append((dp[i-1][1] + dp[i-1][2]) % 1000000009)
        tmp.append((dp[i-2][0] + dp[i-2][2]) % 1000000009)
        tmp.append((dp[i-3][0] + dp[i-3][1]) % 1000000009)
        dp.append(tmp)

    print(sum(dp[N]) % 1000000009)
