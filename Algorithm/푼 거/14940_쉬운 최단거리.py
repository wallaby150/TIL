import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
land = []
q = deque([])
answer = []

for y in range(N):
    line = list(map(int, input().split()))
    tmp = []
    for x in range(M):
        if line[x] == 2:
            tmp.append(0)
            q.append((y, x))
        elif line[x] == 1:
            tmp.append(-1)
        else:
            tmp.append(0)
    land.append(line)
    answer.append(tmp)

while q:
    ny, nx = q.popleft()
    for ty, tx in ((ny - 1, nx),
                   (ny, nx + 1),
                   (ny + 1, nx),
                   (ny, nx - 1)):
        if 0 <= ty < N and 0 <= tx < M:
            if answer[ty][tx] == -1:
                answer[ty][tx] = answer[ny][nx] + 1
                q.append((ty, tx))

for l in answer:
    print(*l)
