import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
# 학생들의 선호학생 목록 저장
wants = dict()
orders = []
for _ in range(N ** 2):
    a, *b = map(int, input().split())
    orders.append(a)
    wants[a] = set(b)

# 인근 학생들의 위치를 저장할 grid 생성
grid = [[0] * N for _ in range(N)]

# 자리 앉히기
for s in orders:
    good = empty = -1
    pt = px = 0
    for y in range(N):
        for x in range(N):
            # 빈 자리라면
            if grid[y][x] == 0:
                now_good = now_empty = 0
                # 주위 자리 탐색
                for ty, tx in [(y - 1, x),
                               (y, x + 1),
                               (y + 1, x),
                               (y, x - 1)]:
                    if 0 <= ty < N and 0 <= tx < N:
                        if grid[ty][tx] in wants[s]:
                            now_good += 1
                        elif not grid[ty][tx]:
                            now_empty += 1

                if now_good > good or (now_good == good and now_empty > empty):
                    good = now_good
                    empty = now_empty
                    py, px = y, x
    grid[py][px] = s

ans = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        targets = wants[grid[y][x]]
        for ty, tx in [(y-1, x),
                       (y, x+1),
                       (y+1, x),
                       (y, x-1)]:
            if 0 <= ty < N and 0 <= tx < N:
                if grid[ty][tx] in targets:
                    cnt += 1

        ans += [0, 1, 10, 100, 1000][cnt]

print(ans)