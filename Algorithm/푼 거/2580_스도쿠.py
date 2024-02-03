import sys
input = lambda : sys.stdin.readline().rstrip()

greed = []
blank = []

for y in range(9):
    tmp = list(map(int, input().split()))
    for x in range(9):
        if tmp[x] == 0:
            blank.append([y, x])
    greed.append(tmp)

bl = len(blank)


def solve(idx):
    if idx == bl:
        for line in greed:
            print(*line)
        return True

    ny, nx = blank[idx]
    visited = [0] * 10
    visited[0] = 1

    # 가로 줄 체크
    for num in greed[ny]:
        visited[num] = 1

    # 세로 줄 체크
    for y in range(9):
        num2 = greed[y][nx]
        visited[num2] = 1

    # 사각형 체크
    sx = nx // 3 * 3
    sy = ny // 3 * 3

    for i in range(3):
        for j in range(3):
            num3 = greed[sy+i][sx+j]
            visited[num3] = 1

    for v in range(1, 10):
        if visited[v] == 0:
            greed[ny][nx] = v
            if solve(idx+1):
                return True
            greed[ny][nx] = 0

solve(0)
