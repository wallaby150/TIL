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
        melt = []

        # 한 덩어리인지 확인과 동시에
        # 어떤 게 녹는지 확인
        visited = set()
        for ice in ices:
            y, x = ice

            stack = [[y, x]]
            visited.add((y, x))
            while stack:
                ny, nx = stack.pop()
                num = grid[ny][nx]
                flag = False
                for ty, tx in [(ny-1, nx),
                               (ny, nx+1),
                               (ny+1, nx),
                               (ny, nx-1)]:
                    if 0 <= ty < N and 0 <= tx < M:
                        if grid[ty][tx] == 0:
                            num -= 1
                            flag = True
                        else:
                            if (ty, tx) not in visited:
                                visited.add((ty, tx))
                                stack.append([ty, tx])
                if flag:
                    melt.append([ny, nx, num])
            break

        if visited != ices:
            print(cnt)
            break

        # 녹은 거 처리
        cnt += 1
        for my, mx, tn in melt:
            tn = max(tn, 0)
            grid[my][mx] = tn
            if tn == 0:
                ices.remove((my, mx))

    else:
        # 다 녹았는데 분리되지 않음.
        print(0)
