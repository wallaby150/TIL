import sys
input = lambda : sys.stdin.readline().rstrip()

D, P = map(int, input().split())
pipes = [list(map(int, input().split())) for _ in range(P)]
pipes.sort(key=lambda x: -x[1])
dp = [-1] * (D+1)
dp[0] = 2 ** 23

for l, c in pipes:
    for i in range(D-l, -1, -1):
        if dp[i] != -1:
            if dp[i+l] == D:
                print(c)
                exit()
            dp[i+l] = max(c, dp[i+l])

print(dp[-1])