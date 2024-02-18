import sys
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
greed = [list(input()) for _ in range(R)]


def solve():
    for y in range(R):
        for x in range(C):
            if greed[y][x] == 'S':
                for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C:
                        if greed[ny][nx] == 'W':
                            return 0
    return 1


ans = solve()

print(ans)
if ans:
    for line in greed:
        for char in line:
            if char == '.':
                print('D', end='')
            else:
                print(char, end='')
        print()