import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
tube = []
visited = [[-1] * N for _ in range(N)]
q = deque()

viruses = []

for y in range(N):
    tmp = list(map(int, input().split()))
    for x in range(N):
        now = tmp[x]
        if now != 0:
            visited[y][x] = 0
            viruses.append((now, y, x))
    tube.append(tmp)

viruses.sort()  # 바이러스를 번호순으로 정렬

S, Y, X = map(int, input().split())
Y, X = Y - 1, X - 1

# 이미 바이러스가 있다면 굳이 안 돌림
if tube[Y][X] != 0:
    print(tube[Y][X])
    exit()

for virus in viruses:
    q.append(virus)

while q:
    if tube[Y][X] != 0:
        break

    virus_type, ny, nx = q.popleft()

    if visited[ny][nx] >= S:
        continue

    for dy, dx in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        togo_y, togo_x = ny + dy, nx + dx
        if 0 <= togo_y < N and 0 <= togo_x < N:
            if visited[togo_y][togo_x] == -1:
                visited[togo_y][togo_x] = visited[ny][nx] + 1
                tube[togo_y][togo_x] = virus_type
                q.append((virus_type, togo_y, togo_x))

print(tube[Y][X])
