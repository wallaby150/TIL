import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = 0

    start = 0

    for num in A:
        diff = 1000000000
        tmp = start
        for idx in range(tmp, W):
            now = abs(num - B[idx])
            if now < diff:
                start = idx
                diff = now
            else:
                C += B[start]
                break
        else:
            C += B[start]

    print(C)
