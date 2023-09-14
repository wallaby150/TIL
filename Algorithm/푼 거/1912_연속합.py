import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))
ans = S[0]

for i in range(1, N):
    S[i] = max(S[i-1] + S[i], S[i])
    if ans < S[i]:
        ans = S[i]
print(ans)
