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

    for i in range(9):
        visited[greed[ny][i]] = 1
        visited[greed[i][nx]] = 1
        num = greed[ny // 3 * 3 + i // 3][nx // 3 * 3 + i % 3]
        visited[num] = 1

    for v in range(1, 10):
        if visited[v] == 0:
            greed[ny][nx] = v
            if solve(idx+1):
                return True
            greed[ny][nx] = 0

solve(0)
