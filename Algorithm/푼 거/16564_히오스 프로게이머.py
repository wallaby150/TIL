import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
X = list(int(input()) for _ in range(N))
X.sort()
n = 0

for i in range(N-1):
    n = i
    tmp = (X[i+1] - X[i]) * (i + 1)
    if tmp <= K:
        X[0] = X[i+1]
        K -= tmp
    else:
        break
else:
    n += 1

if N == 1:
    print(X[0] + K)
else:
    X[0] += K // (n+1)
    print(X[0])
