import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [[0] * N for _ in range(N)]

# 사과 갯수
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    grid[y-1][x-1] = 2

# 방향 전환 정보
L = int(input())
change = []
for _ in range(L):
    tmp = list(input().split())
    change.append((int(tmp[0]), tmp[1]))

time = 0
# 상우하좌
way = 1
snake = [[0, 0]]
grid[0][0] = 1

while True:
    time += 1
    hy, hx = snake[-1]

    ty, tx = hy + [-1, 0, 1, 0][way], hx + [0, 1, 0, -1][way]
    # 벽과 부딪히면 끝
    if ty < 0 or N-1 < ty or tx < 0 or N-1 < tx:
        break
    # 자기 몸이 있어도 끝
    elif grid[ty][tx] == 1:
        break

    # 사과가 없으면
    if grid[ty][tx] != 2:
        tail_y, tail_x = snake.pop(0)
        grid[tail_y][tail_x] = 0
    grid[ty][tx] = 1
    snake.append([ty, tx])

    # 방향 전환
    if change and time == change[0][0]:
        t, d = change.pop(0)
        # 왼쪽으로 꺾는 거면
        if d == 'L':
            # 지금 상이었으면 좌, 아니면 왼쪽으로
            way = (way-1) % 4
        else:
            way = (way+1) % 4

print(time)
