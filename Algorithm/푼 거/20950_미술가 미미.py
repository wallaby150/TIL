import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
target = list(map(int, input().split()))
ans = 255 * 3 + 1

for num in range(2, min(N, 7) + 1):
    for c in combinations(colors, num):
        r, g, b = 0, 0, 0
        for i in c:
            r += i[0]
            g += i[1]
            b += i[2]
        r //= len(c)
        g //= len(c)
        b //= len(c)
        tmp = abs(target[0] - r) + abs(target[1] - g) + abs(target[2] - b)
        ans = min(tmp, ans)

print(ans)