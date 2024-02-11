import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    c, d = a, b

    while True:
        if c == d:
            break
        elif c > d:
            d += b
        else:
            c += a

    print(c)
