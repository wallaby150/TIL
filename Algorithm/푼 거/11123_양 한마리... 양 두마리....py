import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    greed = list(list(input()) for _ in range(H))
    answer = 0

    for y in range(H):
        for x in range(W):
            if greed[y][x] == '#' and visited[y][x] == False:
                answer += 1
                stack = [(y, x)]
                visited[y][x] = True
                while stack:
                    ny, nx = stack.pop()
                    for dy, dx in [(ny+1, nx), (ny, nx+1), (ny-1, nx), (ny, nx-1)]:
                        if 0 <= dy < H and 0 <= dx < W:
                            if visited[dy][dx] == False and greed[dy][dx] == '#':
                                visited[dy][dx] = True
                                stack.append((dy, dx))

    print(answer)