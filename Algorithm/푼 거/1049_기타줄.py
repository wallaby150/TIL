import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
p, e = 1000, 1000

for _ in range(M):
    a, b = map(int, input().split())
    p = min(p, a)
    e = min(e, b)

if p >= e * 6:
    print(e * N)
else:
    if p > e * (N % 6):
        tmp = p * (N // 6)
        tmp += e * (N % 6)
    else:
        tmp = p * (N // 6 + bool(N % 6))
    print(tmp)

