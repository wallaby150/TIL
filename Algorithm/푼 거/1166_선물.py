import sys
input = lambda : sys.stdin.readline().rstrip()

N, L, W, H = map(int, input().split())
l, r = 0, max(L, W, H)

for _ in range(100):
    m = (l + r) / 2
    c = (L // m) * (W // m) * (H // m)
    if c >= N:
        l = m
    else:
        r = m

print(f"{m:.10f}")