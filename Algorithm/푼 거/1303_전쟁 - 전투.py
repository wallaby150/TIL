import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = list(list(input()) for _ in range(M))
visited = list([0] * N for _ in range(M))
score = {'W': 0, 'B': 0}

for y in range(M):
    for x in range(N):
        if visited[y][x] == 0:
            flag = grid[y][x]
            stack = [[y, x]]
            cnt = 1
            visited[y][x] = 1

            while stack:
                ny, nx = stack.pop()
                for dy, dx in [(ny-1, nx),
                               (ny, nx+1),
                               (ny+1, nx),
                               (ny, nx-1)]:
                    if 0 <= dy < M and 0 <= dx < N:
                        if visited[dy][dx] == 0 and grid[dy][dx] == flag:
                            visited[dy][dx] = 1
                            stack.append((dy, dx))
                            cnt += 1
            score[flag] += cnt ** 2

print(*score.values())