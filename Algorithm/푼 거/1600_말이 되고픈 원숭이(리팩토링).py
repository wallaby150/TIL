import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def bfs():
    INF = 10 ** 8
    visited = [[[INF] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 0
    q = deque([(0, 0, 0)])

    while q:
        y, x, jump = q.popleft()
        move = visited[y][x][jump]

        if x == M - 1 and y == N - 1:
            return visited[y][x][jump]

        # 사방으로 갈 수 있는지 확인
        for ty, tx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
            if 0 <= ty < N and 0 <= tx < M and not grid[ty][tx]:
                if visited[ty][tx][jump] == INF:
                    visited[ty][tx][jump] = move + 1
                    q.append((ty, tx, jump))

        # 말처럼 점프할 수 있는지 확인
        if jump < K:
            for dy, dx in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
                jy, jx = y + dy, x + dx
                if 0 <= jy < N and 0 <= jx < M and not grid[jy][jx]:
                    if visited[jy][jx][jump+1] == INF:
                        visited[jy][jx][jump+1] = move + 1
                        q.append((jy, jx, jump+1))

    return -1


print(bfs())
