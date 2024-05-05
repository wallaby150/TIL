import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = list(list(map(int, input().split())) for _ in range(N))
money = list([500] * N for _ in range(N))
visited = list([0] * N for _ in range(N))
ans = 3001

# 각 point마다 돈이 얼마나 드는지 확인
for i in range(1, N - 1):
    for j in range(1, N - 1):
        money[i][j] = grid[i][j] + grid[i - 1][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i][j - 1]


def recur(num, spend, ny, nx):
    global ans

    if spend >= ans:
        return

    if num == 3:
        ans = min(ans, spend)
        return

    for y in range(ny, N-1):
        for x in range(1, N-1):
            # 뒤로 가면 안 됨
            if y == ny and x <= nx:
                continue

            flag = True
            for ty, tx in [(y-1, x),
                           (y, x+1),
                           (y+1, x),
                           (y, x-1),
                           (y, x)]:
                if visited[ty][tx]:
                    flag = False

            if flag:
                for tty, ttx in [(y, x),
                                 (y - 1, x),
                               (y, x + 1),
                               (y + 1, x),
                               (y, x - 1)]:
                    visited[tty][ttx] = 1

                recur(num + 1, spend + money[y][x], y, x)

                for tty, ttx in [(y, x),
                                 (y - 1, x),
                               (y, x + 1),
                               (y + 1, x),
                               (y, x - 1)]:
                    visited[tty][ttx] = 0

recur(0, 0, 1, 0)
print(ans)