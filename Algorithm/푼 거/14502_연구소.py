import sys
from collections import deque
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lab = list(list(map(int, input().split())) for _ in range(N))
blank = []
viruses = []
answer = 0

for y in range(N):
    for x in range(M):
        if lab[y][x] == 0:
            blank.append((y, x))
        elif lab[y][x] == 2:
            viruses.append((y, x))

l = len(blank)
lv = len(viruses)


def search():
    global answer

    count = l - 3 + lv
    now_lab = deepcopy(lab)
    now_v = deque(viruses[:])
    visited = list([0] * M for _ in range(N))
    for v in now_v:
        y, x = v
        visited[y][x] = 1

    # 동서남북
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while now_v:
        vy, vx = now_v.popleft()
        count -= 1

        if answer >= count:
            return

        for way in range(4):
            now_y, now_x = vy + dy[way], vx + dx[way]
            if 0 <= now_y < N and 0 <= now_x < M:
                if visited[now_y][now_x] == 0 and now_lab[now_y][now_x] == 0:
                    now_lab[now_y][now_x] = 2
                    now_v.append((now_y, now_x))
                    visited[now_y][now_x] = 1

    answer = max(count, answer)
    return
        

for first in range(l-2):
    y1, x1 = blank[first]
    lab[y1][x1] = 1
    for second in range(first+1, l-1):
        y2, x2 = blank[second]
        lab[y2][x2] = 1
        for third in range(second+1, l):
            y3, x3 = blank[third]
            lab[y3][x3] = 1
            search()
            lab[y3][x3] = 0
        lab[y2][x2] = 0
    lab[y1][x1] = 0

print(answer)