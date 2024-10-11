import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
ans = [0] * (N + 1)
for i in range(1, N + 1):
    t, p = map(int, input().split())
    ans[i] = max(ans[i-1], ans[i])
    if i + t - 1 <= N:
        ans[i + t - 1] = max(ans[i+t-1], ans[i-1] + p)

print(ans))
