import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = []
sit = []

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] == 5 or a[j] == 2:
            sit.append([i, j])
    grid.append(a)

if ((sit[0][0] - sit[1][0]) ** 2 + (sit[0][1] - sit[1][1]) ** 2) ** 0.5 >= 5:
    sit.sort()
    x, y = min(sit[0][1], sit[1][1]), max(sit[0][1], sit[1][1])
    cnt = 0
    for i in range(sit[0][0], sit[1][0] + 1):
        for j in range(x, y + 1):
            if grid[i][j] == 1:
                cnt += 1
                if cnt >= 3:
                    print(1)
                    exit()
    print(0)
else:
    print(0)
