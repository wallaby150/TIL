import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [[0] * 31 for _ in range(31)]
# y는 H 갯수, x는 W 갯수
for i in range(1, 31):
    dp[0][i] = 1

for x in range(1, 31):
    for y in range(1, x+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]

while True:
    N = int(input())

    if N == 0:
        break

    print(dp[N][N])
