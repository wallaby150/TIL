import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = input(), input()
la, lb = len(A), len(B)
dp = [[''] * (lb+1) for _ in range(la+1)]

for i in range(1, la+1):
    for j in range(1, lb+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + B[j-1]
        else:
            dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]

print(len(dp[-1][-1]))
if len(dp[-1][-1]):
    print(dp[-1][-1])
