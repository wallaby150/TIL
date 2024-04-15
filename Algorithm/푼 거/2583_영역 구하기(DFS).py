import sys
input = lambda : sys.stdin.readline().rstrip()

# 세로, 가로, 직사각형 갯수
M, N, K = map(int ,input().split())
grid = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1


for ny in range(M):
    for nx in range(N):
        if grid[ny][nx] == 0 and visited[ny][nx] == 0:
            stack = [[ny, nx]]
            visited[ny][nx] = 1
            tmp = 0

            while stack:
                sy, sx = stack.pop()
                tmp += 1

                for dy, dx in ((sy-1, sx),
                               (sy, sx+1),
                               (sy+1, sx),
                               (sy, sx-1)):
                    if 0 <= dy < M and 0 <= dx < N:
                        if grid[dy][dx] == 0 and visited[dy][dx] == 0:
                            stack.append([dy, dx])
                            visited[dy][dx] = 1
            ans.append(tmp)

print(len(ans))
print(*sorted(ans))