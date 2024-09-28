import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
hap = [[0] * (M + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, M + 1):
        hap[y][x] = grid[y][x] + hap[y][x-1] + hap[y-1][x] - hap[y-1][x-1]

K = int(input())
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    print(hap[y2][x2] - hap[y2][x1-1] - hap[y1-1][x2] + hap[y1-1][x1-1])
