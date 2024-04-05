import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
jump = [0, 1, 2]

for _ in range(T):
    x, y = map(int, input().split())
    diff = y - x

    while jump[-1] < diff:
        l = len(jump)

        # 홀수 차례면
        if l % 2:
            k = l // 2 + 1
            jump.append(k ** 2)
        else:
            k = l // 2
            jump.append(k ** 2 + k)

    for i in range(len(jump)):
        if jump[i] >= diff:
            print(i)
            break