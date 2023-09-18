import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 우상단부터 시계방향
move_x = [1, 1, 1, 0, -1, -1, -1, 0]
move_y = [-1, 0, 1, 1, 1, 0, -1, -1]

def solve(y, x):
    q = deque([[y, x, 0]])
    visited = list([False] * M for _ in range(N))
    visited[y][x] = True

    while q:
        now_y, now_x, now_count = q.popleft()
        for i in range(8):
            togo_y, togo_x = now_y + move_y[i], now_x + move_x[i]
            if 0 <= togo_y < N and 0 <= togo_x < M:
                if pool[togo_y][togo_x] == 1:
                    return now_count + 1

                else:
                    if visited[togo_y][togo_x] == False:
                        visited[togo_y][togo_x] = True
                        q.append([togo_y, togo_x, now_count + 1])


for Y in range(N):
    for X in range(M):
        if pool[Y][X] == 0:
            ans = max(ans, solve(Y, X))

print(ans)