M, N = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False] * N for _ in range(M)]
x, y = 0, 0
direction = 0
turns = 0

for _ in range(M * N):
    visited[x][y] = True
    nx, ny = x + dx[direction], y + dy[direction]

    if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[nx][ny]:
        direction = (direction + 1) % 4
        turns += 1
        nx, ny = x + dx[direction], y + dy[direction]

    x, y = nx, ny

print(turns - 1)