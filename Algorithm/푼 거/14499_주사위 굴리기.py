import sys
input = lambda : sys.stdin.readline().rstrip()

N, M, y, x, K = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
# 아래, 동, 서, 남, 북, 위
dice = [0, 0, 0, 0, 0, 0]
# 주사위 동서북남
change = {1 : [1, 5, 0, 3, 4, 2],
       2 : [2, 0, 5, 3, 4, 1],
       3 : [3, 1, 2, 5, 0, 4],
       4 : [4, 1, 2, 0, 5, 3]}

coms = list(map(int, input().split()))

# 좌표 동서북남
d = {1 : [0, 1],
     2 : [0, -1],
     3 : [-1, 0],
     4 : [1, 0]}

for com in coms:
    ny, nx = y + d[com][0], x + d[com][1]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
        # 주사위 변경
        tmp = []
        for idx in change[com]:
            tmp.append(dice[idx])
        dice = tmp[:]

        # 주사위 or 바닥 변경
        if grid[ny][nx] == 0:
            grid[ny][nx] = dice[0]
        else:
            dice[0] = grid[ny][nx]
            grid[ny][nx] = 0

        # 윗면 프린트
        print(dice[5])