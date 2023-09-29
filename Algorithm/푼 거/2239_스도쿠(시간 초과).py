import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

sudoku = [list(map(int, input())) for _ in range(9)]

# 3 x 3 크기의
rows = [[0] * 10 for _ in range(9)]
cols = [[0] * 10 for _ in range(9)]
boxes = [[0] * 10 for _ in range(9)]

for i in range(9):
    rows[i][0] = 1
    cols[i][0] = 1
    boxes[i][0] = 1

# 채워야 할 숫자의 위치 저장
targets = deque()

# 타겟의 위치를 저장하고, 각각의 행/열/박스마다 이미 나온 숫자 저장
for y in range(9):
    for x in range(9):
        if sudoku[y][x] == 0:
            targets.append([y, x])

        else:
            rows[y][sudoku[y][x]] = 1
            cols[x][sudoku[y][x]] = 1

            box_num = y // 3 * 3 + x // 3
            boxes[box_num][sudoku[y][x]] = 1


while targets:
    target_y, target_x = targets.popleft()

    now_box = target_y // 3 * 3 + target_x // 3
    possibles = boxes[now_box][:]

    for num in range(1, 10):
        if rows[target_y][num] == 1:
            possibles[num] = 1

        if cols[target_x][num] == 1:
            possibles[num] = 1

    if sum(possibles) == 9:
        ans = possibles.index(0)
        sudoku[target_y][target_x] = ans
        boxes[now_box][ans] = 1
        rows[target_y][ans] = 1
        cols[target_x][ans] = 1
    else:
        targets.append([target_y, target_x])

for r in sudoku:
    print(''.join(list(map(str, r))))