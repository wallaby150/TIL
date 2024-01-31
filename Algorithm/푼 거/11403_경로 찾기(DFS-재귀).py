import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(start):
    for j in range(N):
        if visited[j] == 0 and graph[start][j]:
            visited[j] = 1
            dfs(j)


for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)