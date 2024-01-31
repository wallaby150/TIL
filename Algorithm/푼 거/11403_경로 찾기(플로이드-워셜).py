import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j == k:
                continue

            if not graph[j][k] and graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for line in graph:
    print(*line)