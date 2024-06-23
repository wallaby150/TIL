import sys
input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
L = list(map(int, input().split()))
s = 1
e = 10 ** 10
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for i in L:
        cnt += i // mid

    if cnt >= M:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1

print(ans)
