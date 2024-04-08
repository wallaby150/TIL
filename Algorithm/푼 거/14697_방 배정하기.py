import sys
input = lambda : sys.stdin.readline().rstrip()

A, B, C, N = map(int, input().split())


def solve():
    for i in range(N // A + 1):
        for j in range(N // B + 1):
            for k in range(N // C + 1):
                if A * i + B * j + C * k == N:
                    return True

    else:
        return False


if solve():
    print(1)
else:
    print(0)