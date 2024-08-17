import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
fly = [[-2 * 10 ** 8] * M for _ in range(N)]
land = [[-2 * 10 ** 8] * M for _ in range(N)]
fly[N-1][0] = grid[N-1][0]
land[N-1][M-1] = grid[N-1][M-1]

# 상승비행 루트
for y in range(N-1, -1, -1):
    for x in range(M):
        # 밑에서 날아올 수 있으면
        if y + 1 < N:
            fly[y][x] = fly[y+1][x] + grid[y][x]

        # 왼쪽에서 날 수 있으면
        if x > 0:
            fly[y][x] = max(fly[y][x], fly[y][x-1] + grid[y][x])

# 하강비행 루트
for y in range(N-1, -1, -1):
    for x in range(M-1, -1, -1):
        # 밑에서 날아올 수 있으면
        if y + 1 < N:
            land[y][x] = land[y+1][x] + grid[y][x]

        if x != M-1:
            land[y][x] = max(land[y][x], land[y][x+1] + grid[y][x])


ans = -2 * 10 ** 8
for y in range(N):
    for x in range(M):
        ans = max(ans, fly[y][x] + land[y][x])
print(ans)
