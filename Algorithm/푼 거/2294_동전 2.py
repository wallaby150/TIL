import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
answer = [10001] * (K + 1)
answer[0] = 0
coins = set()

for _ in range(N):
    c = int(input())
    coins.add(c)

for idx in range(1, K + 1):
    for coin in coins:
        if idx - coin >= 0:
            answer[idx] = min(answer[idx], answer[idx - coin] + 1)

if answer[-1] == 10001:
    print(-1)
else:
    print(answer[-1])