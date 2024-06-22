import sys
from collections import Counter
from itertools import chain

input = lambda: sys.stdin.readline().rstrip()

R, C, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]


def calculate_operation(is_row_operation):
    global grid

    if is_row_operation:
        lines = grid
    else:
        lines = list(zip(*grid))  # Transpose for column operations

    new_lines = []
    max_length = 0
    for line in lines:
        counter = Counter(filter(lambda x: x != 0, line))
        sorted_counts = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        new_line = list(chain(*sorted_counts))
        max_length = max(max_length, len(new_line))
        new_lines.append(new_line)

    for i, new_line in enumerate(new_lines):
        new_lines[i] = new_line[:max_length] + [0] * (max_length - len(new_line))

    if not is_row_operation:
        new_lines = list(zip(*new_lines))  # Transpose back

    grid = new_lines
    return len(grid[0]) if is_row_operation else len(grid)  # Update N or M


N, M = 3, 3
for time in range(101):
    if R - 1 < N and C - 1 < M and grid[R - 1][C - 1] == K:
        print(time)
        break

    is_row_operation = M <= N
    if is_row_operation:
        M = calculate_operation(True)
    else:
        N = calculate_operation(False)
else:
    print(-1)
