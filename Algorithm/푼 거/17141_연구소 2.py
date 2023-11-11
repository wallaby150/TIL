import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lab = list(list(map(int, input().split())) for _ in range(N))
blank = []
viruses = []
answer = 10000

for y in range(N):
    for x in range(N):
        if lab[y][x] == 0:
            blank.append((y, x))
        elif lab[y][x] == 2:
            viruses.append((y, x))

lb = len(blank)
lv = len(viruses)
put_place = []


def choice(index, num):
    if num == M:
        search()
        return

    for i in range(index, lv - M + num + 1):
        put_place.append(viruses[i])
        choice(i + 1, num + 1)
        put_place.pop()


def search():
    global answer

    time = 0
    now_v = deque(put_place)
    count = lb + lv - M
    visited = list([-1] * N for _ in range(N))
    for v in now_v:
        y, x = v
        visited[y][x] = 0

    # 동서남북
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while now_v:
        vy, vx = now_v.popleft()

        if answer <= time:
            return

        for way in range(4):
            now_y, now_x = vy + dy[way], vx + dx[way]
            if 0 <= now_y < N and 0 <= now_x < N:
                if visited[now_y][now_x] == -1 and lab[now_y][now_x] in {0, 2}:
                    now_v.append((now_y, now_x))
                    visited[now_y][now_x] = visited[vy][vx] + 1
                    time = visited[vy][vx] + 1
                    count -= 1

    if count == 0:
        answer = min(time, answer)
    return


choice(0, 0)
if answer == 10000:
    print(-1)
else:
    print(answer)
