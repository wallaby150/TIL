puzzle = [input() for _ in range(4)]
total_distance = 0


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for i in range(4):
    for j in range(4):
        if puzzle[i][j] != '.':
            correct_i = (ord(puzzle[i][j]) - ord('A')) // 4
            correct_j = (ord(puzzle[i][j]) - ord('A')) % 4
            total_distance += distance(i, j, correct_i, correct_j)

print(total_distance)