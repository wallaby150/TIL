import sys
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
grid = list(list(map(int, input())) for _ in range(M))
visited = list([0] * N for _ in range(M))


def solve():
    for i in range(N):
        if grid[0][i] == 0 == visited[0][i]:
            stack = [(0, i)]
            while stack:
                y, x, = stack.pop()
                for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                    if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and not grid[ny][nx]:
                        if ny == M-1:
                            return True
                        stack.append((ny, nx))
                        visited[ny][nx] = 1

    return False


if solve():
    print('YES')
else:
    print('NO')
