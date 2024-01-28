import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

H, W, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
start = -1
answer = [[-1] * W for _ in range(H)]
lines = []
coors = []


while True:
    start += 1
    if visited[start][start] == True:
        break

    tmp = deque([])
    tmp_c = deque([])
    y, x = start, start
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        while start <= y + dy < H - start and start <= x + dx < W - start:
            y, x = y + dy, x + dx
            tmp.append(A[y][x])
            tmp_c.append((y, x))
            visited[y][x] = True
    tmp.rotate(1)
    lines.append(tmp)
    tmp_c.rotate(1)
    coors.append(tmp_c)


for i in range(len(lines)):
    line = lines[i]
    coor = coors[i]

    r = R % len(line)
    line.rotate(r)

    while line:
        ny, nx = coor.popleft()
        answer[ny][nx] = line.popleft()


for a in answer:
    print(*a)