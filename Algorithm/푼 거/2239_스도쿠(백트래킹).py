import sys

def is_valid(sudoku, row, col, num):
    # 같은 행, 열, 3x3 박스에 중복된 숫자가 있는지 확인
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num or sudoku[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0  # 해를 찾지 못한 경우 원래 상태로 복원
                return False  # 가능한 모든 숫자를 시도해 봤지만 해를 찾지 못함
    return True  # 모든 칸이 채워져 있거나 스도쿠가 완성된 경우

input = lambda: sys.stdin.readline().rstrip()

sudoku = [list(map(int, input())) for _ in range(9)]

if solve_sudoku(sudoku):
    for row in sudoku:
        print("".join(map(str, row)))
else:
    print("No solution")
