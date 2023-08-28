import sys
# sys.stdin = open("1012_유기농 배추")
input = lambda: sys.stdin.readline().rstrip()


def travel(y, x):
    stack = [[y, x]]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    while stack:
        now_y, now_x = stack.pop()
        for v in range(4):
            togo_y, togo_x = now_y+dy[v], now_x+dx[v]
            if 0 <= togo_y <= N-1 and 0 <= togo_x <= M-1:
                if maps[togo_y][togo_x] == 1 and visited[togo_y][togo_x] == 0:
                    visited[togo_y][togo_x] = 1
                    stack.append([togo_y, togo_x])


for tc in range(int(input())):
# 가로길이, 세로길이, 배추 위치 갯수
    M, N, K = map(int, input().split())
    maps = list([0] * M for _ in range(N))
    visited = list([0] * M for _ in range(N))
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for y in range(N):
        for x in range(M):
            if maps[y][x] == 1 and visited[y][x] == 0:
                count += 1
                travel(y, x)
    print(count)