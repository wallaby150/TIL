import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = [(0, 0, 0)]  # (부순 벽의 수, y, x)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

while q:
    broke, ny, nx = heapq.heappop(q)

    if ny == N-1 and nx == M-1:
        print(broke)
        break

    if visited[ny][nx]:
        continue

    visited[ny][nx] = True

    for dy, dx in directions:
        ty, tx = ny + dy, nx + dx
        if 0 <= ty < N and 0 <= tx < M and not visited[ty][tx]:
            if grid[ty][tx] == 1:
                heapq.heappush(q, (broke + 1, ty, tx))
            else:
                heapq.heappush(q, (broke, ty, tx))