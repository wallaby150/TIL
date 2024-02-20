import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
greed = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(N):
    y, x = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            greed[i][j] = 1

for k in range(100):
    for l in range(100):
        ans += greed[k][l]

print(ans)