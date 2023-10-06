import sys
input = lambda : sys.stdin.readline().rstrip()

# 공의 갯수 N, 바구니 갯수 K
N, K = map(int, input().split())
base = (K + 1) * K / 2
tmp = N

if base > N:
    print(-1)
else:
    tmp -= base
    if tmp % K:
        print(K)
    else:
        print(K-1)