import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
dp = [0] * (K + 1)
bags = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    w, v = bags[i]
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
