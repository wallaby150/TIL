import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
dp = [1, 1, 2, 2, 3, 3]
tmp = 5

for _ in range(T):
    N = int(input())
    if tmp < N:
        l = tmp
        for i in range(tmp + 1, N + 1):
            dp.append((dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009)
            l += 1
        tmp = l
    print(dp[N])

print(dp)