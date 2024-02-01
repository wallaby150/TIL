import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
K = int(input())
answer = 0
coins = [list(map(int, input().split())) for _ in range(K)]
answer = [0] * (T + 1)
answer[0] = 1

for coin, cnt in coins:
    for money in range(T, 0, -1):
        for i in range(1, cnt + 1):
            if money - coin * i >= 0:
                answer[money] += answer[money - coin * i]

print(answer[T])