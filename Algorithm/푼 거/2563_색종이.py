import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
greed = [[0] * 100 for _ in range(100)]
xm, ym = 0, 0
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    xm, ym = max(xm, x + 10), max(ym, y + 10)

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            greed[i][j] = 1

for k in range(ym):
    for l in range(xm):
        ans += greed[k][l]

print(ans)