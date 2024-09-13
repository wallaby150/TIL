import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
stand = [['S'] * M for _ in range(N)]
ans = 0
direction = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


def attack(x, y, d):
    nx, ny, power = x, y, 1
    cnt = 0
    dy, dx = direction[d]

    while power and 0 <= nx < M and 0 <= ny < N:
        power -= 1
        if stand[ny][nx] == 'S':
            stand[ny][nx] = 'F'
            tmp = grid[ny][nx]
            power = max(power, grid[ny][nx] - 1)
            cnt += 1
        ny, nx = ny + dy, nx + dx

    return cnt


def defense(x, y):
    stand[y][x] = 'S'


for _ in range(R):
    Y, X, D = input().split()
    X, Y = int(X) - 1, int(Y) - 1
    if stand[Y][X] == 'S':
        ans += attack(X, Y, D)
    Y, X = map(int, input().split())
    defense(X - 1, Y - 1)

print(ans)
for line in stand:
    print(' '.join(map(str, line)))