import sys
input = lambda: sys.stdin.readline().rstrip()

N, W = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N - 1):
    if coin[i] < coin[i + 1]:
        if W // coin[i] > 0:
            cnt = W // coin[i]
            W = W % coin[i]

    elif cnt and coin[i] > coin[i - 1]:
        W += cnt * coin[i]
        cnt = 0

if cnt != 0:
    W += cnt * coin[-1]

print(W)