import sys
input = lambda: sys.stdin.readline().rstrip()

grid = [list(map(int, input().split())) for _ in range(19)]
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def is_valid(y, x):
    return 0 <= y < 19 and 0 <= x < 19

def find_winner():
    for y in range(19):
        for x in range(19):
            if grid[y][x] != 0:
                color = grid[y][x]
                for dy, dx in directions:
                    count = 1
                    ny, nx = y + dy, x + dx

                    # 진행 방향대로 확인
                    while is_valid(ny, nx) and grid[ny][nx] == color:
                        count += 1
                        ny += dy
                        nx += dx

                        if count > 5:
                            break

                    # 역방향도 확인
                    by, bx = y - dy, x - dx
                    if is_valid(by, bx) and grid[by][bx] == color:
                        continue

                    # 오목인지 확인
                    if count == 5:
                        return color, y + 1, x + 1

    return 0

result = find_winner()
if result == 0:
    print(result)
else:
    print(result[0])
    print(result[1], result[2])