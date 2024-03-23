import sys
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
grid = list(list(map(int, input())) for _ in range(M))
visited = list([0] * N for _ in range(M))

for i in range(N):
    if grid[0][i] == 0 == visited[0][i]:
        stack = [(0, i)]
        while stack:
            y, x, = stack.pop()
            
