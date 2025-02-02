import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]

    count = 0

    for col in range(n):
        floor = m - 1

        for row in range(m - 1, -1, -1):
            if grid[row][col] == 1:
                count += floor - row
                floor -= 1

    print(count)
