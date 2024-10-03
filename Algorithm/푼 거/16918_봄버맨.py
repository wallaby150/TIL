import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, T = map(int, input().split())


def explode(grid):
    tmp = [['O'] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'O':
                tmp[y][x] = '.'

                for dy, dx in ((-1, 0),
                               (0, 1),
                               (1, 0),
                               (0, -1)):
                    ty, tx = y + dy, x + dx
                    if 0 <= ty < N and 0 <= tx < M:
                        tmp[ty][tx] = '.'
    return tmp


if T == 1:
    for _ in range(N):
        print(input())

elif T % 2 == 0:
    for _ in range(N):
        print('O' * M)
# 초기 상태
else:
    grid = [input() for _ in range(N)]
    now = explode(grid)
    if T % 4 == 1:
        now = explode(now)

    for line in now:
        print(''.join(line))
