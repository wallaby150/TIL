import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
count = 0

coins = list(int(input()) for _ in range(N))

for coin in coins[::-1]:
    share = K // coin
    if share:
        K %= coin
        count += share
    if K == 0:
        break

print(count)