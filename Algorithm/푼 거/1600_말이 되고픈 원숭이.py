import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[[10 ** 8] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0
q = deque([(0, 0, 0, 0)])

while q:
    y, x, jump, move = q.popleft()

    # 사방으로 갈 수 있는지 확인
    for ty, tx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
        if 0 <= ty < N and 0 <= tx < M and not grid[ty][tx]:
            if min(visited[ty][tx][:jump + 1]) > move + 1:
                visited[ty][tx][jump] = move + 1
                q.append((ty, tx, jump, move + 1))

    # 말처럼 점프할 수 있는지 확인
    if jump < K:
        for dy, dx in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            jy, jx = y + dy, x + dx
            if 0 <= jy < N and 0 <= jx < M and not grid[jy][jx]:
                if min(visited[jy][jx][:jump + 2]) > move + 1:
                    visited[jy][jx][jump+1] = move + 1
                    q.append((jy, jx, jump+1, move + 1))

ans = min(visited[-1][-1])
print(-1 if ans == 10 ** 8 else ans)
