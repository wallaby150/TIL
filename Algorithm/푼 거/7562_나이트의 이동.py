import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def bfs(start, end, l):
    q = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    matrix = [[0] * l for _ in range(l)]

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        x, y = q.popleft()
        if [x, y] == end:
            return matrix[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True
                matrix[nx][ny] = matrix[x][y] + 1


T = int(input())
for _ in range(T):
    L = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))
    ans = bfs(now, target, L)
    print(ans)
