import sys
input = lambda: sys.stdin.readline().rstrip()

cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break

    ans = v // p * l + min(l, v % p)
    print(f'Case {cnt}: {ans}')
    cnt += 1