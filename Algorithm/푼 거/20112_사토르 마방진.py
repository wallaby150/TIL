import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] != grid[j][i]:
                return "NO"
    return "YES"


N = int(input())
grid = [input() for _ in range(N)]

print(solve(N, grid))
