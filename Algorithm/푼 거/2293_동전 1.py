import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
answer = [0] * (K + 1)
coins = set(int(input()) for _ in range(N))
answer[0] = 1


for coin in coins:
    for i in range(coin, K+1):
        answer[i] += answer[i-coin]

print(answer[-1])