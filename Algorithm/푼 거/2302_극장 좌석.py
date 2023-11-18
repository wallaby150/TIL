import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
vip = list(int(input()) for _ in range(M))
count = 1
dp = [1, 1, 2]
for i in range(3, N+1):
    dp.append(dp[i-1]+dp[i-2])

if M > 0:
    tmp = 0
    for j in range(M):
        count *= dp[vip[j] - 1 - tmp]
        tmp = vip[j]
    count *= dp[N - tmp]
else:
    count *= dp[N]

print(count)