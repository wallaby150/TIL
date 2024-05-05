import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = list(list(map(int, input().split())) for _ in range(N))
ans = 3001
candis = []

for y in range(1, N-1):
    for x in range(1, N-1):
        candis.append([y, x])


def solve(comb):
    global ans
    money = 0
    visited = set()

    for ny, nx in comb:
        if (ny, nx) in visited:
            return

        money += grid[ny][nx]

        for ty, tx in [(ny-1, nx),
                       (ny, nx+1),
                       (ny+1, nx),
                       (ny, nx-1)]:
            if (ty, tx) in visited:
                return
            visited.add((ty, tx))
            money += grid[ty][tx]

    ans = min(ans, money)


for tmp in combinations(candis, 3):
    solve(tmp)

print(ans)
