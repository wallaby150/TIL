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
        l, r = start, W-1
        while l < r:
            m = (l+r) // 2
            if B[m] <= num:
                l = m + 1
            else:
                r = m
        start = l
        if l == 0:
            C += B[0]
        else:
            C += B[l] if num - B[l-1] > B[l] - num else B[l-1]

    print(C)
