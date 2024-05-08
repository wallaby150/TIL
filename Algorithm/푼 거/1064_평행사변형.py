import sys
input = lambda: sys.stdin.readline().rstrip()

ax, ay, bx, by, cx, cy = map(int, input().split())

if (ax - bx) * (ay - cy) == (ay - by) * (ax - cx):
    print(-1.0)
else:
    ab_l = ((ax-bx) ** 2 + (ay-by) ** 2) ** 0.5
    ac_l = ((ax-cx) ** 2 + (ay-cy) ** 2) ** 0.5
    bc_l = ((bx-cx) ** 2 + (by-cy) ** 2) ** 0.5

    l = [ab_l + ac_l, ab_l + bc_l, ac_l + bc_l]
    ans = (max(l) - min(l)) * 2
    print(ans)
