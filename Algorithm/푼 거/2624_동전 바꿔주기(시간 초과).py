import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
K = int(input())
answer = 0
coins = [list(map(int, input().split())) for _ in range(K)]
coins.sort(reverse=True)


def solve(idx, rest):
    global answer

    if rest == 0:
        answer += 1
        return

    if idx >= K:
        return

    coin = coins[idx][0]
    for i in range(min(coins[idx][1], rest // coin)):
        solve(idx + 1, rest - coin * i)


solve(0, T)
print(answer)