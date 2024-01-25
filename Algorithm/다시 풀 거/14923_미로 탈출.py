import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

H, W = map(int, input().split())
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
high = 10000000
visited = [[[high, high] for _ in range(W)] for _ in range(H)]
visited[sy-1][sx-1][0] = 0
visited[sy-1][sx-1][1] = 0


q = deque([[sy-1, sx-1, 0]])
while q:
    ny, nx, did = q.popleft()

    if ny == ey-1 and nx == ex-1:
        break

    for d in range(4):
        # 상하좌우
        ty, tx = ny + [-1, 0, 1, 0][d], nx + [0, 1, 0, -1][d]
        # 범위 안이고
        if 0 <= tx < W and 0 <= ty < H:
            # 갈 수 있고
            if grid[ty][tx] == 0:
                # 안 갔으면
                if visited[ty][tx][did] == high:
                    if did == 1 and visited[ty][tx][0] <= visited[ny][nx][1]:
                        continue
                    visited[ty][tx][did] = visited[ny][nx][did] + 1
                    q.append([ty, tx, did])

            # 벽이 막혀있는데 아직 능력 안 썼으면
            elif did == 0:
                tty, ttx = ty + [-1, 0, 1, 0][d], tx + [0, 1, 0, -1][d]
                # 범위 안이고
                if 0 <= ttx < W and 0 <= tty < H:
                    # 벽이 아니고
                    if grid[tty][ttx] == 0:
                        # 안 가봤고
                        if visited[ty][tx][1] == high:
                            # 능력을 쓴 것보다 빠르면
                            if visited[ny][nx][0] + 2 < visited[tty][ttx][0]:
                                visited[tty][ttx][1] = visited[ny][nx][0] + 2
                                q.append([tty, ttx, 1])


a, b = visited[ey-1][ex-1]
if a == high and b == high:
    print(-1)
else:
    print(min(a, b))