import sys
input = lambda: sys.stdin.readline().rstrip()


def turn_grid(g, t, l):
    if t == 0:
        return g

    stick = [[], [], [], g[l//2][::-1]]
    road = [[], [], [], []]

    for i in range(l):
        stick[0].append(g[i][i])
        stick[1].append(g[i][l//2])
        stick[2].append(g[i][l-1-i])
        road[0].append((i, i))
        road[1].append((i, l//2))
        road[2].append((i, l-1-i))
        road[3].append((l//2, l-1-i))

    for j in range(4):
        road.append(road[j][::-1])

    for k in range(4):
        ns = stick[k]
        for z in range(l):
            y, x = road[(k + t) % 8][z]
            g[y][x] = ns[z]

    return g


T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    times = (360 + D) % 360 // 45

    for line in turn_grid(grid, times, N):
        print(*line)
