import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = []
dots = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 5 or line[j] == 2:
            dots.append([i, j])
    grid.append(line)


def solve():
    a, b = dots
    if ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 < 5:
        return 0

    cnt = 0
    for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
        for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            if grid[i][j] == 1:
                cnt += 1
                if cnt == 3:
                    return 1
    return 0


print(solve())
