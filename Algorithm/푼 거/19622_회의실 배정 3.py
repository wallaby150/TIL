import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
confs = []
for _ in range(N):
    a, b, c = map(int, input().split())
    confs.append(c)
dp = [0] * (N+1)
dp[1] = confs[0]

for i in range(2, N+1):
    dp[i] = max(dp[i-1], dp[i-2] + confs[i-1])

print(dp[-1])
