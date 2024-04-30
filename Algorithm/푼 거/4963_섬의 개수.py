import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    W, H = map(int, input().split())

    if W == H == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    ans = 0

    for y in range(H):
        for x in range(W):
            if visited[y][x] == 0 and grid[y][x] == 1:
                stack = [[y, x]]
                visited[y][x] = 1

                while stack:
                    ny, nx = stack.pop()

                    for dy, dx in [(ny-1, nx),
                                   (ny, nx+1),
                                   (ny+1, nx),
                                   (ny, nx-1),
                                   (ny-1, nx-1),
                                   (ny-1, nx+1),
                                   (ny+1, nx+1),
                                   (ny+1, nx-1),]:
                        if 0 <= dy < H and 0 <= dx < W:
                            if visited[dy][dx] == 0 and grid[dy][dx] == 1:
                                visited[dy][dx] = 1
                                stack.append([dy, dx])

                ans += 1
    print(ans)