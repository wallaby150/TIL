import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def move_clouds(clouds, d, s):
    dy, dx = directions[d - 1]
    return {((y + dy * s) % N, (x + dx * s) % N) for y, x in clouds}


def rain(clouds):
    for y, x in clouds:
        grid[y][x] += 1


def water_copy(clouds):
    for y, x in clouds:
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] > 0:
                grid[y][x] += 1


def create_new_clouds(old_clouds):
    new_clouds = set()
    for y in range(N):
        for x in range(N):
            if (y, x) not in old_clouds and grid[y][x] >= 2:
                grid[y][x] -= 2
                new_clouds.add((y, x))
    return new_clouds


def simulate(M):
    clouds = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}

    for _ in range(M):
        d, s = map(int, input().split())
        clouds = move_clouds(clouds, d, s)
        rain(clouds)
        water_copy(clouds)
        clouds = create_new_clouds(clouds)

    return sum(sum(row) for row in grid)


print(simulate(M))