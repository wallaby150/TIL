import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = input(), input()
dp = [0] * len(B)

for i in range(len(A)):
    cnt = 0
    for j in range(len(B)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif A[i] == B[j]:
            dp[j] = cnt + 1

print(max(dp))
