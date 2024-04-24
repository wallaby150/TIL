import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A, B = map(int, input().split())
dots = set(tuple(map(int, input().split())) for _ in range(N))
ans = 0

for dot in dots:
    x, y = dot
    if (x + A, y) in dots and (x, y + B) in dots and (x + A, y + B) in dots:
        ans += 1

print(ans)