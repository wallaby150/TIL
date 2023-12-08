import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    players = [0] * 10001
    for _ in range(N):
        for num in map(int, input().split()):
            players[num] += 1

    second = sorted(list(set(players)))[-2]
    answer = []
    for idx in range(1, 10001):
        if players[idx] == second:
            answer.append(idx)

    print(*answer)
