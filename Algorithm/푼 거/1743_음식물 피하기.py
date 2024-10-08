import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
togos = {tuple(map(int, input().split())) for _ in range(K)}
checked = set()
ans = 0

while togos:
    y, x = togos.pop()
    cnt = 1
    stack = [(y, x)]
    while stack:
        ny, nx = stack.pop()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ty, tx = ny + dy, nx + dx
            if (ty, tx) in togos:
                stack.append((ty, tx))
                togos.remove((ty, tx))
                cnt += 1
    ans = max(cnt, ans)

print(ans)
