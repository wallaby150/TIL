import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    stack = [i]
    while stack:
        num = stack.pop()
        for j in range(N):
            if visited[i][j] == 0 and graph[num][j]:
                visited[i][j] = 1
                stack.append(j)

for line in visited:
    print(*line)