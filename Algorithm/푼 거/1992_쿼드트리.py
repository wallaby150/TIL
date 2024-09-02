import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(input()) for _ in range(N)]


def solve(y, x, size):
    if size == 1:
        return grid[y][x]

    tmp = ''
    for i in range(4):
        m = size // 2
        ty, tx = [(y, x), (y, x + m), (y + m, x), (y + m, x + m)][i]
        tmp += solve(ty, tx, m)

    if tmp == '1111':
        return '1'
    elif tmp == '0000':
        return '0'
    else:
        return f'({tmp})'


print(solve(0, 0, N))
