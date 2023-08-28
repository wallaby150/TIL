import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
# 남, 동, 북, 서
dir = 0
now = (0, 0)
routes = {(0, 0)}

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for char in input():
    if char == "R":
        if dir != 3:
            dir += 1
        else:
            dir = 0
    elif char == "L":
        if dir != 0:
            dir -= 1
        else:
            dir = 3
    else:
        x, y = now[0] + dx[dir], now[1] + dy[dir]
        now = (x, y)
        routes.add((x, y))

# print(routes)

a = sorted(routes)
b = sorted(routes, key=lambda z: z[1])
# print(a)
# print(b)

width = a[-1][0] - a[0][0] + 1
height = b[-1][1] - b[0][1] + 1

# print(width)
# print(height)

maps = [['#']*width for _ in range(height)]
for dot in routes:
    ny = b[-1][1] - dot[1]
    nx = width -1 - abs(a[-1][0]-dot[0])


    # print(dot, ny, nx)
    maps[ny][nx] = '.'

for line in maps:
    print(line)