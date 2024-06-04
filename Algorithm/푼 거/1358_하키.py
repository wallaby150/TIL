import sys
input = lambda: sys.stdin.readline().rstrip()

W, H, X, Y, P = map(int, input().split())
ans = 0

for _ in range(P):
    x, y = map(int, input().split())
    if X <= x <= X + W and Y <= y <= Y + H:
        ans += 1
    else:
        for tx, ty in [(X, Y+H/2), (X+W, Y+H/2)]:
            if (x-tx) ** 2 + (y-ty) ** 2 <= (H/2) ** 2:
                ans += 1
                break

print(ans)
