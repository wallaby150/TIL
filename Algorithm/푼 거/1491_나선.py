import sys
input = lambda : sys.stdin.readline().rstrip()

# 가로, 세로
M, N = map(int, input().split())
maps = list([0]*M for _ in range(N))
# print(maps)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

maps[N-1][0] = 1
queue = [(N-1, 0)]
d = 0
while queue:
    now = queue.pop()
    for _ in range(4):
        togo_y, togo_x = now[0] + dy[d], now[1] + dx[d]
        if 0 <= togo_y < N and 0 <= togo_x < M and maps[togo_y][togo_x] == 0:
            maps[togo_y][togo_x] = 1
            queue.append((togo_y, togo_x))
            break
        else:
            d += 1
            d %= 4


# print(now)
print(now[1], N - now[0] - 1)