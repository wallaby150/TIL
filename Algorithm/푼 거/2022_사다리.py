import sys
input = lambda: sys.stdin.readline().rstrip()

x, y, c = map(float, input().split())
s, e = 0, min(x, y)


def get_c(m):
    a = (x ** 2 - m ** 2) ** 0.5
    b = (y ** 2 - m ** 2) ** 0.5
    tmp = (a * b) / (a + b)
    return (a * b) / (a + b)


ans = 0
while e - s > 0.000001:
    mid = (s + e) / 2
    if get_c(mid) >= c:
        ans = mid
        s = mid
    else:
        e = mid

print(f"{round(ans, 4)}")
