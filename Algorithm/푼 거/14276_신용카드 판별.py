import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    card = list(map(int, input()))

    for i in range(0, 15, 2):
        x = card[i] * 2
        card[i] = x // 10 + x % 10

    total = sum(card)
    print("T" if total % 10 == 0 else "F")
