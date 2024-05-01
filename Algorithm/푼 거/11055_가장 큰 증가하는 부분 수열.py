import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
ans[0] = A[0]

for i in range(N):
    ans[i] = A[i]
    for j in range(0, i):
        if A[j] < A[i]:
            ans[i] = max(ans[i], ans[j] + A[i])

print(max(ans))
