import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
tube = []
viruses = [[] for _ in range(K+1)]
visited = list([-1] * N for _ in range(N))
q = deque()

for y in range(N):
    tmp = list(map(int, input().split()))
    for x in range(N):
        now = tmp[x]
        if now != 0:
            viruses[now].append((y, x))
            visited[y][x] = 0
    tube.append(tmp)

S, Y, X = map(int, input().split())
Y, X = Y-1, X-1

# 이미 바이러스가 있다면 굳이 안 돌림
if tube[Y][X] != 0:
    print(tube[Y][X])
    exit()

for virus in viruses:
    q.extend(virus)

while q:
    # 해당 칸에 운명이 정해져있다면 안 돌림
    if tube[Y][X] != 0:
        break

    ny, nx = q.popleft()
    # 동서남북

    if visited[ny][nx] >= S:
        continue

    type = tube[ny][nx]

    for dy, dx in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        togo_y, togo_x = ny + dy, nx + dx
        # 벗어나있지 않고
        if 0 <= togo_y < N and 0 <= togo_x < N:
            # 가본 적이 없으면
            if visited[togo_y][togo_x] == -1:
                visited[togo_y][togo_x] = visited[ny][nx] + 1
                tube[togo_y][togo_x] = type
                q.append((togo_y, togo_x))

print(tube[Y][X])

