import sys
input = lambda: sys.stdin.readline().rstrip()

# 세로 N, 가로 M
N, M = map(int, input().split())
grid = []
ices = set()

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] > 0:
            ices.add((i, j))
    grid.append(tmp)

if len(ices) == N * M or len(ices) == 0:
    print(0)
else:
    cnt = 0
    # 얼음이 있는 동안
    while ices:
        cnt += 1
        melt = []

        # 어떤 게 녹는지 확인
        for ice in ices:
            y, x = ice
            num = grid[y][x]
            flag = False
            for ty, tx in [(y-1, x),
                           (y, x+1),
                           (y+1, x),
                           (y, x-1)]:
                if 0 <= ty < N and 0 <= tx < M:
                    if grid[ty][tx] == 0:
                        num -= 1
                        flag = True
                    if num == 0:
                        break
            if flag:
                melt.append([y, x, num])

        # 녹은 거 처리
        for my, mx, tn in melt:
            grid[my][mx] = tn
            if tn == 0:
                ices.remove((my, mx))

        # 한 덩어리인지 확인
        visited = set()
        for iy, ix in ices:
            visited.add((iy, ix))
            stack = [(iy, ix)]

            while stack:
                ny, nx = stack.pop()
                for tty, ttx in [(ny - 1, nx),
                               (ny, nx + 1),
                               (ny + 1, nx),
                               (ny, nx - 1)]:
                    if 0 <= tty < N and 0 <= ttx < M:
                        if grid[tty][ttx] > 0 and (tty, ttx) not in visited:
                            visited.add((tty, ttx))
                            stack.append((tty, ttx))
            break

        # 한 덩어리인지 확인
        if visited != ices:
            print(cnt)
            break

    else:
        # 다 녹았는데 분리되지 않음.
        print(0)